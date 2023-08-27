import numpy as np

# Data
data = [
    (240000, 3650),
    (139800, 3800),
    (150500, 4400),
    (185530, 4450),
    (176000, 5250),
    (114800, 5350),
    (166800, 5800),
    (89000, 5990),
    (144500, 5999),
    (84000, 6200),
    (82029, 6390),
    (63060, 6390),
    (74000, 6600),
    (97500, 6800),
    (67000, 6800),
    (76025, 6900),
    (48235, 6900),
    (93000, 6990),
    (60949, 7490),
    (65674, 7555),
    (54000, 7990),
    (68500, 7990),
    (22899, 7990),
    (61789, 8290)
]

# Convert data into NumPy arrays
data = np.array(data)

# Extract mileage and prices
mileage = data[:, 0]
prices = data[:, 1]

# Calculate required values
n = len(data)
sum_mileage = np.sum(mileage)
sum_prices = np.sum(prices)
sum_mileage_squared = np.sum(mileage ** 2)
sum_mileage_prices = np.sum(mileage * prices)

# Calculate regression coefficients
m = (n * sum_mileage_prices - sum_mileage * sum_prices) / (n * sum_mileage_squared - sum_mileage ** 2)
b = (sum_prices * sum_mileage_squared - sum_mileage * sum_mileage_prices) / (n * sum_mileage_squared - sum_mileage ** 2)

# Given mileage
given_mileage = 240000

# Predict price using the regression line equation
predicted_price = m * given_mileage + b

# Print the regression equation and predicted price
print(f"Regression equation: y = {m}x + {b}")
print(f"Predicted price for mileage {given_mileage}: {predicted_price}")
