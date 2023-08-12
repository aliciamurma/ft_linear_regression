import sys
import csv
import os.path
import re
import pandas as pd
import matplotlib.pyplot as plt

# tmp0 = learningRate * 1/m suma(estimatePrice(mileage[i]) - price[i])
# tmp1 = learningRate * 1/m suma(estimatePrice(mileage[i]) - price[i]) * mileage[i]
# tmpTheta0 = learningRate * 1/m * Σ(estimatePrice(mileage[i] - price[i])) tmpTheta1 = learningRate * 1/m * Σ(estimatePrice(mileage[i] - price[i])) * mileage[i]

# Update the thetas
def get_gradient(mileage, price, theta0, theta1, learningRate):
    temp0 = 0
    temp1 = 0
    for i in range(len(mileage)):
        temp0 += theta0 + theta1 * mileage[i] - price[i]
        temp1 += (theta0 + theta1 * mileage[i] - price[i]) * mileage[i]
    theta0 -= (learningRate * temp0) / len(mileage)
    theta1 -= (learningRate * temp1) / len(mileage)
    return theta0, theta1

# Calculate the error
def get_error(theta0, theta1, price, mileage):
    error = 0
    for i in range(len(mileage)):
        predictedPrice = theta0 + (theta1 * mileage[i])
        error += (predictedPrice - price[i]) ** 2
    error /= (2 * len(mileage))
    return error

def main():
    price = []
    mileage = []
    theta0 =  0.0
    theta1 =  0.0
    iterations = 1000
    learningRate = 0.001

    try:
        with open("data.csv", 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header
            for row in csv_reader:
                price.append(float(row[0]))
                mileage.append(float(row[1]))

        # Normalize mileage data (optional but can help stability)
        max_mileage = max(mileage)
        min_mileage = min(mileage)
        normalized_mileage = [(x - min_mileage) / (max_mileage - min_mileage) for x in mileage]

        # Training loop
        for i in range(iterations):
            theta0, theta1 = get_gradient(normalized_mileage, price, theta0, theta1, learningRate)
            error = get_error(theta0, theta1, price, normalized_mileage)

        with open('thetas.txt', 'w') as file:
            file.write(f"{theta0} {theta1}\n")
        print("Trained!")

    except Exception as e:
        print("Error 1: ", e)

if __name__ == "__main__": 
    main()