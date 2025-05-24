# SOA-Competition

# EDFIP Project - Premium Calculation

This repository contains the code used for calculating premiums as part of the EDFIP project.

## Project Status

The project has been completed, and this code was used for the initial submission. However, please note that the logic in the code **may have some logical errors** and will be revisited for improvements in the future.

## Description

- The code attempts to calculate insurance premiums based on dam failure probabilities, hazard levels, and housing data across different regions.
- It reads dam data from a CSV file, filters relevant entries, adjusts probabilities for a one-year period, and calculates expected losses.
- Premiums are calculated for three regions ("Flumevale," "Lyndrassia," and "Navaldia"), considering different hazard multipliers, house values, and participation rates.
- The code applies inflation adjustment for premium collection over multiple years and uses scaling to match target inflows.

## Code Explanation

- **Data Input:** Loads a CSV file containing dam data, filters for entries related to "Earth" dams, and cleans missing values.
- **Probability Adjustment:** Adjusts the failure probability for a 1-year time frame based on the original 10-year probability.
- **Hazard Multipliers:** Applies risk multipliers based on hazard levels ("Low," "Significant," "High," etc.).
- **Regional Data:** Uses predefined housing counts and failure probabilities for each region.
- **Participation Rates:** Incorporates participation factors both by region and by house value category to model insurance uptake.
- **Premium Calculation:**  
  - Calculates expected loss as a basis for premium setting.  
  - Computes region-specific premiums scaled by hazard proportions and failure probabilities.  
  - Calculates premiums per house value category within each region, factoring in weights for house values.  
  - Adjusts for inflation over the coverage period.  
  - Applies final scaling to ensure total premiums collected match the target inflow.
- **Output:** Prints total premiums per region, premiums by house value category, and average annual premium per insured house.

## Disclaimer

This code was developed as part of a student project and may contain logical errors or assumptions that need revision. It is provided for reference and learning purposes. The premium calculation logic will be revisited in future versions.

## How to Use

1. Clone the repository.
2. Ensure the input CSV file path is correct or replace it with your own data.
3. Run the main Python script to see premium calculations.
4. Modify parameters or extend the script as needed.

---

Thank you for reviewing this work.
