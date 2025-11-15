# SOA Competition - EDFIP Project Repository

This repository contains analysis and modeling work submitted for the **EDFIP Project** in the **2025 SOA Competition**. It includes four main components covering exploratory data analysis, inflation forecasting, loss analysis, and premium calculation.

---

## Repository Structure

```
SOA-Competition/
│
├── EDA/
│   ├── main.py
│   └── README.md              # Exploratory data analysis documentation
│
├── inflation_forecasting/
│   ├── inflation_forecasting.R
│   └── README.md              # Inflation forecasting model documentation
│
├── earth-dam-loss-analysis/
│   ├── earth_dam_loss_analysis.py
│   └── README.md              # Loss analysis explanation
│
├── premium_calculations/
│   ├── premium_calculations.py
│   └── README.md              # Premium pricing model explanation
│
└── README.md                  # This parent overview file
```

---

## 1. Exploratory Data Analysis (EDA)

The EDA module performs comprehensive data exploration and visualization on dam failure and economic datasets. It includes:

- Data loading and preprocessing utilities
- Statistical summaries and distribution analysis
- Correlation analysis between variables
- Visualization functions for loss patterns and risk factors
- Missing data analysis

For full documentation, see:  
[`EDA/README.md`](./EDA/README.md)

---

## 2. Inflation Forecasting

This R script forecasts inflation rates using time series analysis with ARIMAX models. It:

- Loads historical economic data including inflation, GDP growth, and unemployment
- Performs stationarity tests (ADF, KPSS)
- Fits ARIMAX models with economic predictors
- Forecasts 21 years of inflation rates
- Generates diagnostic plots and forecast visualizations

For full documentation, see:  
[`inflation_forecasting/README.md`](./inflation_forecasting/README.md)

---

## 3. Earth Dam Loss Analysis

This script processes dam failure and financial loss data, filtered for **Earth-type dams**, and:

- Filters dataset by dam type
- Calculates average losses per region:
  - Property Loss (Qm)
  - Liability Loss (Qm)
  - Business Interruption Loss (Qm)
- Adjusts annual probability of failure to a 10-year equivalent
- Outputs:
  - Regional summaries to console
  - A grouped bar chart visualizing average losses by region

For full documentation, see:  
[`earth-dam-loss-analysis/README.md`](./earth-dam-loss-analysis/README.md)

---

## 4. Premium Calculation Model

This module estimates insurance premiums for properties affected by dam-related risk, incorporating:

- Region-specific failure probabilities and hazard classifications
- House value categories and participation rates
- Inflation adjustments over multi-year coverage terms
- Detailed formulas for probability conversion, expected loss, and premium allocation
- A scaling mechanism to align collected premiums with expected inflows

For full documentation including mathematical formulas, see:  
[`premium_calculations/README.md`](./premium_calculations/README.md)

---

## Requirements

### Python Components (EDA, Loss Analysis, Premium Calculation)

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn (for EDA)

Install Python dependencies with:

```bash
pip install pandas numpy matplotlib seaborn
```

### R Components (Inflation Forecasting)

- R 4.x or higher
- Required packages: forecast, tseries, ggplot2, readr, scales

Install R dependencies with:

```r
install.packages(c("forecast", "tseries", "ggplot2", "readr", "scales"))
```

---

## Usage

Each module is self-contained with its own data requirements and run instructions.

### Python Scripts

```powershell
# Run EDA
cd EDA
python main.py

# Run Premium Calculations
cd premium_calculations
python premium_calculations.py

# Run Loss Analysis
cd earth-dam-loss-analysis
python earth_dam_loss_analysis.py
```

### R Scripts

```powershell
# Run Inflation Forecasting
cd inflation_forecasting
Rscript inflation_forecasting.R
```

Refer to individual component READMEs for specific data file requirements and expected outputs.

---

## Data Files

- `EDA/data/` - Input datasets for exploratory analysis
- `inflation_forecasting/data/economic_data.csv` - Historical economic indicators
- `premium_calculations/data/data.csv` - Dam failure and loss data
- `earth-dam-loss-analysis/data/data.csv` - Dam loss dataset

---