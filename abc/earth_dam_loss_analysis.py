import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# File path
input_file = r"C:\Pyhton\PyCharm Community Edition 2024.2.1\Files\WEbScraping\SOA Competition\data\srcsc-2025-dam-data-for-students.csv"

# Read data
df = pd.read_csv(input_file)

# Filter data for 'Earth' primary type
df = df[df["Primary Type"] == 'Earth']

# Group by region
regions = df.groupby("Region")

# Store calculated averages for plotting
region_names = []
property_losses = []
liability_losses = []
business_losses = []

# Loop through each region and calculate required values
for region_name, region_df in regions:
    region_name_clean = str(region_name).replace("(", "").replace(")", "").replace("'", "").replace(",", "")

    # Compute mean values
    region_df["Probability of Failure"] = 1 - (1 - df["Probability of Failure"])**(1/10)
    prob_failure = region_df["Probability of Failure"].mean()
    property_loss = region_df["Loss given failure - prop (Qm)"].mean().round(2)
    liability_loss = region_df["Loss given failure - liab (Qm)"].mean().round(2)
    business_loss = region_df["Loss given failure - BI (Qm)"].mean().round(2)
    height = region_df["Height (m)"].mean().round(2)
    inspection_freq = region_df["Inspection Frequency"].mean().round(2)

    # Print information for each region
    print(f"============={region_name_clean}============")
    print(f"Prob of Failure: {prob_failure}")
    print(f"Property Loss (Qm): {property_loss}")
    print(f"Liabilities Loss (Qm): {liability_loss}")
    print(f"Business Interruptions Loss (Qm): {business_loss}")
    print(f"Height (m): {height}")
    print(f"Inspection Frequency: {inspection_freq}\n")

    # Append data for graph
    region_names.append(region_name_clean)
    property_losses.append(property_loss)
    liability_losses.append(liability_loss)
    business_losses.append(business_loss)

# Convert lists to numpy arrays
regions_count = len(region_names)
x = np.arange(3)  # 3 loss categories
width = 0.15  # Adjust bar width based on the number of regions

# Define color shades for the theme (forest green variations)
colors = [
    "#34590C",
    "#62A818",
    "#95E03B"
]

# Plot bars for each region in each loss category
plt.figure(figsize=(10, 6))

bars = []  # Store bars for legend

for i, region in enumerate(region_names):
    bar = plt.bar(
        x + (i * width),
        [property_losses[i], liability_losses[i], business_losses[i]],
        width,
        color=colors[i % len(colors)],  # Rotate through green shades  # Apply hatch patterns
        edgecolor="black",  # Keep black borders for clarity
    )
    bars.append(
        Patch(facecolor=colors[i % len(colors)], edgecolor="black",
              label=region))

# Formatting the plot
plt.xlabel("Loss Types")
plt.ylabel("Average Loss (Qm)")
plt.title("Losses by Type for Each Region (Earth Dams)")
plt.xticks(x + (width * (regions_count - 1) / 2),
           ["Property", "Liabilities", "BI"])  # Centering x-ticks

# Fixing the legend with visible patterns
plt.legend(handles=bars, title="Regions", bbox_to_anchor=(1.05, 1), loc="upper left", fontsize=10)

plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show plot
plt.tight_layout()
plt.show()


df["Probability of Failure"] = 1 - (1 - df["Probability of Failure"])**(1/10)

print(df["Probability of Failure"].mean())
