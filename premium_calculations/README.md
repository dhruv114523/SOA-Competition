
# SOA-Competition
# EDFIP Project - Premium Calculation

This document explains how `premium_calculations/premium_calculations.py` computes insurance premiums. It lists inputs, constants, and the exact formulas used in the script. Where the script uses external constants or placeholders, this README notes them and explains expected values.

## Purpose

Compute region- and house-value-category-level insurance premiums for earthen dams using observed loss estimates, failure probabilities, hazard multipliers, participation rates, and an inflation adjustment for multi-year coverage.

## Required input

- `data/data.csv` with the following columns used by the script:
  - `Primary Type` (filtered to "Earth")
  - `Probability of Failure` (originally a 10-year probability)
  - `Loss given failure - liab (Qm)` (liability losses, Qm indicates millions)
  - `Loss given failure - prop (Qm)` (property losses)
  - `Loss given failure - BI (Qm)` (business interruption losses)
  - `Region` (region name)
  - `Hazard` (hazard category: Low, Significant, High, Undetermined, etc.)

The script also expects numeric region-level constants defined inside the file (houses per region, failure probabilities, participation rates, house value categories and weights).

## Key constants in the script

- Hazard multipliers: hazard_multipliers = {"Low": 1.0, "Significant": 1.5, "High": 2.5, "Undetermined": 1.2}
- Houses per region: a dictionary of three-element lists representing counts for each house value category (see file for exact numbers).
- Failure probabilities per region: numeric values multiplied by 0.8 in the script.
- Participation rates per region and per house-value category. Example formula used in file: participation = base_rate / sqrt(4/3).
- House value weights: [0.7, 1.3, 5.5]
- inflation_rate = 0.041

## Variables and units

- Loss columns use the suffix `Qm`. In the script a factor of `1e6` is used when converting expected loss to nominal currency units. Treat values in `Loss given failure - liab (Qm)` as millions before multiplication by 1e6.
- `expected_loss` in the script is computed in the same units as the losses prior to multiplying by `1e6` for display or target inflow scaling.

## Formulas used in the script

Below are the formulas implemented (symbolic form), with brief explanations of each variable.

1) Convert a 10-year failure probability p_10 to a 1-year probability p_1:

  p_1 = 1 - (1 - p_10)^(1/10)

  This is implemented as:
  df["Probability of Failure"] = 1 - (1 - df["Probability of Failure"]) ** (1 / 10)

2) Expected loss (pre-insured-scaling):

  For each dam i, loss_i = Loss_given_failure_liab_i (in Q millions)
  p1_i = 1-year probability for dam i

  expected_loss_raw = sum_i (loss_i * p1_i)

  The script multiplies this by an insured fraction taken from another module:

  expected_loss = expected_loss_raw * insured_scale

  where insured_scale = 0.322474 (the script documents this comes from `insured_percentage.py`).

  Note: the code converts to nominal units for the target inflow by multiplying by `1e6` later on.

3) Base target inflow and inflation adjustment:

  base_target_inflow = expected_loss * 0.5 * 1e6

  The factor 0.5 represents the portion of expected loss used as the base target inflow in the script.

  The script adjusts this for multi-year coverage using the `adjust_for_inflation` function. The implemented function computes the cumulative growth factor for a sequence of payments or inflows at constant nominal rate r over `years`:

  adjust_for_inflation(amount, years) = amount * ( (1 + r)^years - 1 ) / r

  with r = inflation_rate (0.041 in the script). This is equivalent to the sum of a geometric series: amount * sum_{t=1..years} (1+r)^{t-1}.

  The final `target_inflow` used for scaling premiums is:

  target_inflow = adjust_for_inflation(base_target_inflow, years)

4) Cumulative region risk across `years` (Poisson-exponential approximation):

  cumulative_risk = 1 - exp(-years * lambda_region)

  where lambda_region is the per-year failure probability for the region (the script uses `failure_probabilities[region]`). This gives the probability of at least one failure over `years` assuming a Poisson process.

5) Raw regional premium share (before scaling):

  region_raw_share = (total_houses_region * lambda_region) / total_risk_exposure

  region_premium_raw = region_raw_share * cumulative_risk * participation_factor * hazard_weighted_premium

  Notes:
  - `total_risk_exposure` and `hazard_weighted_premium` are referenced in the code but not computed within this file. They act as normalizing or scaling constants. If not defined externally, the script will raise a NameError. In a complete workflow, `total_risk_exposure` should equal the sum across regions of `total_houses_region * lambda_region` or a similar aggregate exposure measure, and `hazard_weighted_premium` should summarize hazard multiplier effects across regions using `hazard_proportions` and `hazard_multipliers`.

6) Category-level premium allocation within a region:

  For house value category j in region r:

  effective_houses_{r,j} = num_houses_{r,j} * house_value_participation_j * region_participation_r

  weighted_contribution_{r,j} = ( effective_houses_{r,j} * house_value_weight_j ) / ( total_houses_region * sum_k house_value_weight_k )

  category_premium_{r,j} = region_premium_r * weighted_contribution_{r,j}

  This allocates the region-level premium to value categories based on participation-adjusted counts and the value weights.

7) Average premium per insured house (annualized):

  avg_premium_per_house_{r} = region_premium_r / total_effective_houses_region

  For the category-level average annual premium the script computes:

  num_insured_houses_{r,j} = num_houses_{r,j} * house_value_participation_j * region_participation_r

  avg_annual_premium_{r,j} = (category_premium_{r,j} / num_insured_houses_{r,j}) / years

8) Final scaling to match target inflow:

  final_collected_premium = sum_r region_premium_r
  region_scaling_factor = target_inflow / final_collected_premium
  region_premium_r := region_premium_r * region_scaling_factor

  Each region's category premiums are scaled proportionally so that the total collected premium equals the `target_inflow`.

## Example notes and interpretation

- The script stores losses in `Qm` units (millions). When computing monetary targets the code multiplies by `1e6` to express amounts in base currency units.
- The insured scale (`0.322474`) is crucial: it reduces the raw expected loss to the portion that is expected to be insured. Confirm its derivation in `insured_percentage.py` before using the output for policy design.

## Running the script

1. Place the input CSV at `premium_calculations/data/data.csv`.
2. From the project root run:

```powershell
cd premium_calculations
python premium_calculations.py
```