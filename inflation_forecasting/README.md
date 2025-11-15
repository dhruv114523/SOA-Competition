## inflation_forecasting.R

This script builds and visualizes a multi-year inflation forecast using an ARIMAX model.

Purpose
- Provide a reproducible routine to load historical economic data, fit an ARIMAX model to the inflation series with selected exogenous regressors, and produce a 21-year forecast with a plot and table of results.

Quick contract
- Input: a CSV file at `data/economic_data.csv` with at least the columns `Year`, `Inflation`, `Government_of_Tarrodan_Overnight_Rate`, and `1-yr_Risk_Free_Annual_Spot_Rate`.
- Output: a printed data frame of projected inflation values and a plot showing historical and forecasted inflation from 2020 to 2045.

Requirements
- R (stable release).
- The script uses these R packages: `forecast`, `tseries`, `ggplot2`, `readr`, and `scales`.

Install required packages
Run the following in an R session to install missing packages:

```r
install.packages(c("forecast", "tseries", "ggplot2", "readr", "scales"))
```

Input data expectations
- File path: `data/economic_data.csv`, relative to the `inflation_forecasting` directory when the script is run.
- Required columns:
  - `Year` (numeric or integer)
  - `Inflation` (percentage values, may include a percent sign)
  - `Government_of_Tarrodan_Overnight_Rate` (percentage values)
  - `1-yr_Risk_Free_Annual_Spot_Rate` (percentage values)
- Notes: the script strips percent signs and converts the relevant columns to numeric. Ensure that CSV is UTF-8 encoded if it contains special characters.

Usage
1. Open a terminal or PowerShell in the `inflation_forecasting` folder.
2. Make sure the `data` subfolder contains `economic_data.csv` with the required columns.
3. Run the script with Rscript:

```powershell
Rscript inflation_forecasting.R
```

What the script does (high level)
- Loads packages and the CSV file with `readr::read_csv`.
- Cleans column names and numeric percentage fields.
- Builds a time series object for the inflation series.
- Uses `forecast::auto.arima` with external regressors to fit an ARIMAX model.
- Constructs a 21-row future exogenous regressor matrix and forecasts 21 periods ahead.
- Produces a combined table of recent historical values (from 2020) and the 21-year forecast.
- Plots the combined series using `ggplot2` with percent formatting on the y axis.

Files
- `inflation_forecasting.R`: main script.
- `data/economic_data.csv`: input CSV expected by the script.