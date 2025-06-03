from utilities import *

# Load the dataset
df = load_data("data/srcsc-2025-dam-data-for-students.csv")

summarize_data(df)

# Top 10 analysis
top_10_by_feature(df, "Height (m)", "Height")
top_10_by_feature(df, "Length (km)", "Length")
top_10_by_feature(df, "Volume (m3)", "Volume")

# Plot histogram for Year Completed
plot_histogram(df)

# Plot trends
plot_trends(df)

plot_ma_dam_trends(df)

built_by_year(df)

top_5_dam_purpose(df)

inspection_frequency(df)

count_of_hazard(df)

top_10_for_each_type(df)
