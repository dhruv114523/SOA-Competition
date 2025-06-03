# Load necessary libraries
library(forecast)
library(tseries)
library(ggplot2)
library(readr)

# Load dataset using UTF-8 encoding
file_path <- "data/economic_data.csv"  
data <- read_csv(file_path)

# Clean column names
colnames(data) <- gsub(" ", "_", colnames(data))

# Convert percentage columns to numeric
data$Inflation <- as.numeric(gsub("%", "", data$Inflation))
data$Government_of_Tarrodan_Overnight_Rate <- as.numeric(gsub("%", "", data$Government_of_Tarrodan_Overnight_Rate))
data$Risk_Free_1yr <- as.numeric(gsub("%", "", data$`1-yr_Risk_Free_Annual_Spot_Rate`))

# Sort data
data <- data[order(data$Year), ]

# Create time series object
inflation_ts <- ts(data$Inflation, start = min(data$Year), frequency = 1)

# Define external regressors
xreg_matrix <- cbind(data$Government_of_Tarrodan_Overnight_Rate, data$Risk_Free_1yr)

# Fit ARIMAX model
best_arimax <- auto.arima(inflation_ts, xreg = xreg_matrix)

# Forecasting: Define future exogenous variables
future_xreg <- matrix(rep(tail(xreg_matrix, 1), 21), nrow = 21, byrow = TRUE)

# Generate forecast
inflation_forecast <- forecast(best_arimax, xreg = future_xreg, h = 21)

# Prepare forecast results
forecast_results <- data.frame(
  Year = (max(data$Year) + 1):(max(data$Year) + 21), 
  Forecast = inflation_forecast$mean
)

# Combine with historical data
historical_data <- data[data$Year >= 2020, c("Year", "Inflation")]
colnames(historical_data) <- c("Year", "Forecast")
combined_data <- rbind(historical_data, forecast_results)

# Plot final forecast with clean styling
ggplot(combined_data, aes(x = Year, y = Forecast)) +
  geom_line(color = "#660000", size = 1.5) +
  scale_y_continuous(labels = scales::percent_format(scale = 1)) +
  scale_x_continuous(breaks = seq(2020, 2045, 1)) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  labs(title = "Projected Inflation Rate (2020-2045)", 
       x = "Year", 
       y = "Projected Inflation Rate")

# Print forecast values
colnames(forecast_results) <- c("Year", "Projected Inflation Rate (%)")
print(forecast_results)
