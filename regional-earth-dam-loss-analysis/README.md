# Earth Dam Loss Analysis by Region

## Overview

This Python project analyzes financial loss data associated with **Earth-type dams**, grouped by geographic **region**. The script processes a dataset to calculate average property, liability, and business interruption losses, and visualizes these metrics in a **bar chart** comparing regions.

## Features

- Filters dataset to include only dams with **Primary Type = 'Earth'**
- Calculates average values per region for:
  - Property Loss (Qm)
  - Liability Loss (Qm)
  - Business Interruption Loss (Qm)
  - Dam Height (m)
  - Inspection Frequency
  - Adjusted 10-year Probability of Failure
- **Prints per-region summaries** to the console
- **Plots a grouped bar chart** comparing average losses by region
- Uses a custom color palette with region-based legends

## File Structure

```
earth-dam-loss-analysis/
│
├── data/
│   └── data.csv                  # Input dataset
│
├── earth_dam_loss_analysis.py   # Main Python script
│
└── README.md                     # This file
```

## Requirements

- Python 3.x
- pandas
- numpy
- matplotlib

Install dependencies with:

```bash
pip install pandas numpy matplotlib
```

## How to Use

1. Place your dataset in the `data/` folder and name it `data.csv`.
2. Run the script from the terminal or an IDE:

```bash
python earth_dam_loss_analysis.py
```

3. The script will:
   - Print regional summaries to the console
   - Display a bar chart comparing average losses by type and region

## Output

### Console Example

```
=============NorthWest============
Prob of Failure: 0.0123
Property Loss (Qm): 6.85
Liabilities Loss (Qm): 2.13
Business Interruptions Loss (Qm): 3.79
Height (m): 45.6
Inspection Frequency: 2.0
```

### Chart

A bar chart showing:
- X-axis: Loss types (Property, Liabilities, BI)
- Y-axis: Average loss in Qm
- Multiple bars per group, each representing a region

## Notes

- The script adjusts the annual probability of failure to a **10-year equivalent** using:
  ```
  P_10yr = 1 - (1 - P_annual)^(1/10)
  ```
- The chart adjusts dynamically based on how many regions are present after filtering for Earth dams.
- Region names are cleaned for display purposes.

## License

This project is provided for educational, analytical, and visualization purposes. You may reuse or adapt the code with attribution.
