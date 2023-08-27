import numpy as np

# Datos de ejemplo
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

# Parámetros del modelo
theta0 = 8496.714655063388
theta1 = -0.021421526484220323

# Predicciones del modelo
predictions = theta0 + theta1 * mileage

# Cálculo del error cuadrático medio (MSE)
mse = np.mean((predictions - prices) ** 2)
print("Error cuadrático medio (MSE):", mse)

# Cálculo del error absoluto medio (MAE)
mae = np.mean(np.abs(predictions - prices))
print("Error absoluto medio (MAE):", mae)

total_variance = np.var(prices)
explained_variance = np.var(predictions)
r_squared = explained_variance / total_variance
print("Coeficiente de determinación R²:", r_squared)