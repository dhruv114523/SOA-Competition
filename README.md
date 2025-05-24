# SOA-Competition
# EDFIP Project - Premium Calculation

This repository contains the code used for calculating insurance premiums as part of the EDFIP project.

## Project Status

The project has been completed, and this code was used for the initial submission. However, please note that the logic in the code **may have some logical errors** and will be revisited for improvements in the future.

## Description

- The code attempts to calculate insurance premiums for Earth-type dams based on dam failure probabilities, hazard levels, house values, and regional factors.
- The premium calculation incorporates adjustments for inflation, participation rates, hazard multipliers, and multi-year coverage periods.
- It produces premium amounts broken down by region and house value categories.

## Code Explanation

- **Data Input and Filtering:**  
  Reads data from a CSV file and filters it for "Earth" type dams. It also handles missing values in loss amounts.

- **Probability Adjustment:**  
  Converts the 10-year failure probability to a 1-year period probability for calculations.

- **Hazard Multipliers:**  
  Applies multipliers to account for hazard levels classified as Low, Significant, High, or Undetermined.

- **Regional Data:**  
  Defines the number of houses per region and house value categories, participation rates, and dam failure probabilities.

- **Inflation Adjustment:**  
  Uses a function `adjust_for_inflation()` to adjust premiums for expected inflation over the coverage period.

- **Premium Calculation (`calculate_premium(years)`):**  
  Calculates expected losses, adjusts for insured percentage, and computes premiums per region and house category.  
  It factors in participation rates, hazard weights, and applies a scaling mechanism to align collected premiums with target inflows.

- **Output:**  
  Prints total premiums collected by region and by house value category, along with average annual premiums per insured house.

## Disclaimer

This implementation is an early version and **may contain logical errors** in the premium calculation method. The code will be revisited and improved based on further review and feedback.

## How to Use

- Clone this repository.
- Ensure the CSV input file `data/data.csv` is in place with the expected columns.
- Run the main script to perform premium calculations and display results.
- Modify parameters such as coverage years or input data as needed.

---

Thank you for reviewing this work.

