import pandas as pd
import numpy as np
import math

# Read CSV file
input_file = r'data/data.csv'
df = pd.read_csv(input_file)

# Filter for "Earth" type
df = df[df["Primary Type"] == "Earth"] #Insurance Policy only for Earthen Dam Failures
df = df[df["Distance to Nearest City (km)"] != ""]

# Adjust probability of failure for a 1-year period
df["Probability of Failure"] = 1 - (1 - df["Probability of Failure"]) ** (1 / 10) # Converting to 1 year period

# Replace missing values for loss amounts
df["Loss given failure - liab (Qm)"] = df["Loss given failure - liab (Qm)"].fillna(0)
df["Loss given failure - prop (Qm)"] = df["Loss given failure - prop (Qm)"].fillna(0)
df["Loss given failure - BI (Qm)"] = df["Loss given failure - BI (Qm)"].fillna(0)

# Hazard level multipliers
hazard_multipliers = {"Low": 1.0, "Significant": 1.5, "High": 2.5, "Undetermined": 1.2}

# Compute the proportion of dams in each hazard category for each region
hazard_proportions = df.groupby(["Region", "Hazard"]).size().unstack(fill_value=0)
hazard_proportions = hazard_proportions.div(hazard_proportions.sum(axis=1), axis=0)
print(hazard_proportions.sum(axis=1))

# Ensure "Undetermined" is handled
for hazard in hazard_proportions.columns:
    if hazard not in hazard_multipliers:
        hazard_multipliers[hazard] = 1.2  # Default multiplier for unexpected categories

# Number of houses per region
houses_per_region = {
    "Flumevale": [446_720 + 552_111 + 887_815, 1_219_671 + 2_730_435 + 2_521_934, 5_165_736+ 2_386_698],
    "Lyndrassia": [206_960 + 414_955 + 471_356, 448_956+572_280+ 532_740, 268_786 + 51_349],
    "Navaldia": [871_223 + 1_593_970 + 2_169_919, 2_505_863 + 3_816_207 + 3_189_802, 1_825_774 + 351_150],
}

# Dam failure probabilities per region
failure_probabilities = {
    "Flumevale": 0.08703230318802861*0.8, "Lyndrassia": 0.09536593434343434*0.8, "Navaldia": 0.09537536422259374*0.8
}

# Participation rates
region_participation = {"Flumevale": 0.5/(math.sqrt(4/3)), "Lyndrassia": 0.7/(math.sqrt(4/3)), "Navaldia": 0.7/(math.sqrt(4/3))}
house_value_participation = [0.5/(math.sqrt(4/3)), 0.7/(math.sqrt(4/3)), 0.9/(math.sqrt(4/3))]

# House value categories and weights
house_value_ranges = ["Less than Q150,000", "Q150,000 to Q499,999", "Q500,000 or more"]
house_value_weights = [0.7, 1.3, 5.5]

inflation_rate = 0.041

def adjust_for_inflation(amount, years):
    """Adjusts premium collection for inflation using a discounted present value approach."""
    return amount * ((1 + inflation_rate) ** years - 1) / ((1 + inflation_rate) - 1)

def calculate_premium(years):
    """Calculate fair insurance premiums per region and house category with hazard proportion adjustments."""

    # Compute total expected loss
    prob_times_loss = df["Loss given failure - liab (Qm)"] * df["Probability of Failure"]
    expected_loss = prob_times_loss.sum() * 0.322474 #Got this from insured_percentage.py

    """
    Got 0.322474 from insured_percentage.py, result is number of houses insured
    """
    print(f"asduhawiudhwhdiuaw {expected_loss*1e6:,}")
    # Adjust Target Inflow for Multi-Year Policies
    base_target_inflow = expected_loss * 0.5 * 1e6
    target_inflow = adjust_for_inflation(base_target_inflow, years)

    region_premiums = {}
    category_premiums = {region: [] for region in houses_per_region}
    avg_premium_per_house = {}
    avg_premium_per_house_category = {region: [] for region in houses_per_region}

    total_collected_premium = 0

    # Calculate risk-based regional premiums
    for region, houses in houses_per_region.items():
        participation_factor = region_participation[region]
        cumulative_risk = 1 - np.exp(-years * failure_probabilities[region])

        # Raw regional premium before final scaling
        region_premium = (sum(houses) * failure_probabilities[region] / total_risk_exposure)
        region_premiums[region] = region_premium * cumulative_risk * participation_factor * hazard_weighted_premium

        # Calculate category-level premiums
        total_houses = sum(houses)
        total_effective_houses = sum(num_houses * house_value_participation[i] * participation_factor for i, num_houses in enumerate(houses))

        for i, num_houses in enumerate(houses):
            effective_houses = num_houses * house_value_participation[i] * participation_factor
            weighted_contribution = (effective_houses * house_value_weights[i]) / (total_houses * sum(house_value_weights))
            category_premium = region_premiums[region] * weighted_contribution
            category_premiums[region].append(category_premium)

            total_collected_premium += category_premium

        # Compute the average premium per house for this region
        avg_premium_per_house[region] = region_premiums[region] / total_effective_houses if total_effective_houses > 0 else 0

    # Final Scaling: Adjust collected premiums to match `target_inflow`
    final_collected_premium = sum(region_premiums.values())
    region_scaling_factor = target_inflow / final_collected_premium if final_collected_premium > 0 else 1

    for region in region_premiums:
        region_premiums[region] *= region_scaling_factor

    # Adjust category premiums to match the adjusted `region_premiums`
    for region in region_premiums:
        adjusted_region_premium = region_premiums[region]
        category_total = sum(category_premiums[region])
        if category_total > 0:
            category_scaling_factor = adjusted_region_premium / category_total
            category_premiums[region] = [p * category_scaling_factor for p in category_premiums[region]]

    return region_premiums, category_premiums

# Run premium calculations
# Print final premiums
for years in [1]:
    print(f"\n===== {years}-year coverage (Final Double Scaling) =====")
    region_premiums, category_premiums = calculate_premium(years)

    print(f"Total Premium Collected: {sum(region_premiums.values()):,.2f} Qalkoons")

    for region in region_premiums:
        print(f"\nRegion: {region} | Total Premium: {region_premiums[region]:,.2f} Qalkoons")

        print(f"{'House Value Range':<25} | {'Total Premium (Qalkoons)':<25} | {'Avg Annual Premium per House'}")
        print("-" * 80)

        for i, value_range in enumerate(house_value_ranges):
            num_insured_houses = houses_per_region[region][i] * house_value_participation[i] * region_participation[region]
            avg_annual_premium = (category_premiums[region][i] / num_insured_houses) / years if num_insured_houses > 0 else 0

            print(f"{value_range:<25} | {category_premiums[region][i]:<25,.2f} | {avg_annual_premium:,.2f}")
