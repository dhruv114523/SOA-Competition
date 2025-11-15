## main.py

This script performs exploratory data analysis on the dam dataset provided in the `data` subfolder. It loads the data, runs summary statistics, and produces several analytic tables and plots used in the project.

Purpose
- Provide a lightweight, reproducible EDA pipeline that prepares and visualizes key aspects of the dam dataset so subsequent modelling or reporting can rely on cleaned summaries and figures.

Quick contract
- Input: a CSV file at `data/srcsc-2025-dam-data-for-students.csv` relative to the `EDA` directory.
- Output: console printed summaries and generated plots produced by functions in `utilities.py`.

Dependencies
- Python 3.0
- The script depends on the helper functions implemented in `EDA/utilities.py`. Inspect that file for specific package imports, but common EDA packages likely include `pandas`, `matplotlib`, and `seaborn`.

Input data expectations
- File path: `data/srcsc-2025-dam-data-for-students.csv`.
- The CSV should contain columns referenced by the helper functions. Examples include `Year Completed`, `Height (m)`, `Length (km)`, `Volume (m3)`, dam type, dam purpose, inspection data, and hazard-related fields.
- If column names differ, adjust either the CSV headers or the utility function calls in `main.py`.

What the script runs (summary)
- Loads the dataset via `load_data` from `utilities.py`.
- Runs `summarize_data` for descriptive statistics.
- Produces top-10 lists by feature using `top_10_by_feature` for height, length, and volume.
- Creates histograms and trend plots via `plot_histogram`, `plot_trends`, and `plot_ma_dam_trends`.
- Generates counts and breakdowns including `built_by_year`, `top_5_dam_purpose`, `inspection_frequency`, `count_of_hazard`, and `top_10_for_each_type`.

Running the script
Change directory to the `EDA` folder and run the script with Python:

```powershell
cd EDA
python main.py
```

Files
- `main.py`: entry point for EDA.
- `utilities.py`: helper functions used by `main.py`.
- `data/srcsc-2025-dam-data-for-students.csv`: expected input dataset.
