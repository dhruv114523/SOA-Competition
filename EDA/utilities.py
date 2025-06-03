import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import numpy as np



def inspection_frequency(df):
    # Group by 'Year Completed' and calculate the sum of 'Inspection Frequency' for each year
    sum_freq = df.groupby(["Year Completed"])["Inspection Frequency"].sum()
    mean_freq = df.groupby(["Year Completed"])["Inspection Frequency"].mean()

    # Convert the groups to a tabular format using tabulate
    print(tabulate(sum_freq.reset_index(), headers=["Year Completed", "Total Inspection Frequency"], tablefmt="grid"))
    print("\033[31m-\033[0m"*200)
    print(tabulate(mean_freq.reset_index(), headers = ["Year Completed", "Mean Inspection Frequency"], tablefmt = "grid"))


def load_data(filepath):
    """Load dataset from a CSV file."""
    df = pd.read_csv(filepath)
    return df


def plot_ma_dam_trends(df):
    """
    Plots the average height, volume, and length of dams over time using a dual-axis approach.

    Parameters:
        df (pd.DataFrame): DataFrame containing 'Year Completed', 'Height (m)', 'Volume (m3)', and 'Length (km)' columns.

    Returns:
        None
    """

    years = df.groupby("Year Completed")

    years_plot = []
    height_means = []
    volume_means = []
    length_means = []

    for year, group in years:
        years_plot.append(year)
        height_means.append(group["Height (m)"].mean())
        volume_means.append(group["Volume (m3)"].mean())
        length_means.append(group["Length (km)"].mean())

    fig, ax1 = plt.subplots()

    # Primary y-axis
    ax1.set_xlabel("Year Completed")
    ax1.set_ylabel("Average Height (m) / Length (km)", color="blue")
    ax1.plot(years_plot, height_means, color="blue", label="Avg Height (m)")
    ax1.plot(years_plot, length_means, color="red", label="Avg Length (km)")
    ax1.tick_params(axis="y", labelcolor="blue")

    # Secondary y-axis
    ax2 = ax1.twinx()
    ax2.set_ylabel("Average Volume (m³)", color="green")
    ax2.plot(years_plot, volume_means, color="green", label="Avg Volume (m³)")
    ax2.tick_params(axis="y", labelcolor="green")

    # Title and legend
    fig.suptitle("Dam Statistics Over Time")
    ax1.legend(loc="upper left")
    ax2.legend(loc="upper right")

    plt.show()



def built_by_year(df):
    df = df[df["Year Completed"] > 1940]  # Filter for years after 1940
    year_counts = df["Year Completed"].value_counts().sort_index()

    plt.plot(year_counts.index, year_counts.values, marker="o", linestyle="-", markersize=4)

    # Identify Peak
    peak_idx = year_counts.idxmax()
    peak_val = year_counts.max()
    plt.scatter(peak_idx, peak_val, color="red", zorder=3)  # Mark peak

    plt.annotate(f'Peak ({peak_idx}, {peak_val})',
                 xy=(peak_idx, peak_val),
                 xytext=(peak_idx + 5, peak_val - 5),  # Adjusted for visibility
                 arrowprops=dict(facecolor='black', arrowstyle='->'),
                 fontsize=10)

    plt.xlabel("Year Completed")
    plt.ylabel("Number of Dams Built")
    plt.title("Dams Built Per Year (After 1940)")
    plt.show()



def summarize_data(df):
    """Print basic statistics and missing values count."""
    print(df["Distance to Nearest City (km)"].describe())
    print("Missing values in 'Distance to Nearest City (km)':", df["Distance to Nearest City (km)"].isna().sum())

    print("\n\n")

    print(df["Height (m)"].describe())
    print("Missing values in 'Height (m)':", df["Height (m)"].isna().sum())

    print("\n\n")

    print(df["Volume (m3)"].describe())
    print("Missing values in 'Volume (m3)':", df["Volume (m3)"].isna().sum())

    print("\n\n")

    print(df["Length (km)"].describe())
    print("Missing values in 'Length (km)':", df["Length (km)"].isna().sum())



def plot_histogram(df):
    df = df[df["Year Completed"] > 1940]  # Filter for years after 1940
    value_counts = df["Year Completed"].value_counts()

    bins = 10  # Number of bins
    hist_values, bin_edges, _ = plt.hist(value_counts.index,
                                         weights=value_counts.values,
                                         bins=bins,
                                         edgecolor="black")

    # Find peak
    peak_bin_idx = hist_values.argmax()
    peak_x = (bin_edges[peak_bin_idx] + bin_edges[peak_bin_idx + 1]) / 2
    peak_y = hist_values[peak_bin_idx]

    plt.scatter(peak_x, peak_y, color='red', zorder=3)  # Highlight peak
    plt.annotate(f'Peak ({int(peak_x)}, {int(peak_y)})',
                 xy=(peak_x, peak_y),
                 xytext=(peak_x + 5, peak_y - 5),
                 arrowprops=dict(facecolor='black', arrowstyle='->'),
                 fontsize=10)

    plt.title("Distribution of Year Completed (After 1940)")
    plt.xlabel("Year")
    plt.ylabel("Frequency")
    plt.show()




def top_10_by_feature(df, feature, title):
    #Top 10 dams in each region
    df = df.drop(columns=["Years Modified", "Surface (km2)", "Drainage (km2)", "Spillway",
                          "Last Inspection Date", "Inspection Frequency", "Distance to Nearest City (km)",
                          "Hazard", "Assessment", "Assessment Date", "Probability of Failure",
                          "Loss given failure - prop (Qm)", "Loss given failure - liab (Qm)",
                          "Loss given failure - BI (Qm)"])

    regions = df.groupby(["Region"])



    print(f"\033[1m\033[31mTop 10 by {title}\033[0m\n\n")

    for key, region in regions:
        region = region.sort_values([feature], ascending=False)
        print(key)
        print(tabulate(region.head(10), headers="keys", tablefmt="pretty", showindex=False))
        print("\n\n\n")

def plot_trends(df):
    df = df[df["Year Completed"] > 1940]  # Filter for years after 1940
    years = df.groupby("Year Completed")

    years_plot = []
    height_means = []
    volume_means = []
    length_means = []

    for year, group in years:
        years_plot.append(year)
        height_means.append(group["Height (m)"].mean())
        volume_means.append(group["Volume (m3)"].mean())
        length_means.append(group["Length (km)"].mean())

    # Plot Height Trend
    plt.plot(years_plot, height_means, color="blue")
    peak_idx = np.argmax(height_means)
    plt.scatter(years_plot[peak_idx], height_means[peak_idx], color="red")
    plt.annotate(f'Peak ({years_plot[peak_idx]}, {height_means[peak_idx]:.2f})',
                 xy=(years_plot[peak_idx], height_means[peak_idx]),
                 xytext=(years_plot[peak_idx] + 5, height_means[peak_idx] - 2),
                 arrowprops=dict(facecolor='black', arrowstyle='->'))
    plt.xlabel("Year Completed")
    plt.ylabel("Average Height (m)")
    plt.title("Average Height by Year Completed (After 1940)")
    plt.show()

    # Plot Volume Trend
    plt.plot(years_plot, volume_means, color="green")
    peak_idx = np.argmax(volume_means)
    plt.scatter(years_plot[peak_idx], volume_means[peak_idx], color="red")
    plt.annotate(f'Peak ({years_plot[peak_idx]}, {volume_means[peak_idx]:.2f})',
                 xy=(years_plot[peak_idx], volume_means[peak_idx]),
                 xytext=(years_plot[peak_idx] + 5, volume_means[peak_idx] - 2),
                 arrowprops=dict(facecolor='black', arrowstyle='->'))
    plt.xlabel("Year Completed")
    plt.ylabel("Average Volume (m3)")
    plt.title("Average Volume by Year Completed (After 1940)")
    plt.show()

    # Plot Length Trend
    plt.plot(years_plot, length_means, color="red")
    peak_idx = np.argmax(length_means)
    plt.scatter(years_plot[peak_idx], length_means[peak_idx], color="red")
    plt.annotate(f'Peak ({years_plot[peak_idx]}, {length_means[peak_idx]:.2f})',
                 xy=(years_plot[peak_idx], length_means[peak_idx]),
                 xytext=(years_plot[peak_idx] + 5, length_means[peak_idx] - 2),
                 arrowprops=dict(facecolor='black', arrowstyle='->'))
    plt.xlabel("Year Completed")
    plt.ylabel("Average Length (km)")
    plt.title("Average Length by Year Completed (After 1940)")
    plt.show()



def top_5_dam_purpose(df):
    top_5_in_country = df["Primary Purpose"].value_counts().reset_index()
    top_5_in_country.columns = ["Primary Purpose", "Count"]
    print("top 5 purposes in country")
    print(top_5_in_country.head())
    regions = df.groupby(["Region"])
    for region, group in regions:
        group = group["Primary Purpose"].value_counts()
        print(region)
        print(group.head(5))
        print("\n\n")

def count_of_hazard(df):
    country = df["Hazard"].value_counts()
    print(country)

    regions = df.groupby(["Region"])
    for region, group in regions:
        group = group["Hazard"].value_counts()
        print(region)
        print(group)
        print("-"*100)

def top_10_for_each_type(df):
    groups = df.groupby(["Primary Type"])
    for type_of_dam, group in groups:
        print(f"\033[1m\033[31m-\033[0m"*100)
        print(type_of_dam)
        top_10_by_feature(df, "Height (m)", "Height")
        print("\n\n")
        top_10_by_feature(df, "Volume (m3)", "Volume")
        print("\n\n")
        top_10_by_feature(df, "Length (km)", "Length")
        print(f"\033[1m\033[31m-\033[0m"*100)
        print("\n\n")
