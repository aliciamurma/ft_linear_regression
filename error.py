import sys
import csv
import os.path
import re
import math

def save_square_error(error, R2):
    with open('error.txt', 'w') as file:
        file.write(f"Mean square error: {error}\nRegression coeficient: {R2}\n")

# Mean square error (error cuadrático medio) indicates the quality of the model
# That is the average of the squares of the differences between the predicted and actual vales (el cuadrado de la diferencia)
# Lowest - better
def calculate_mean_square_error(actual_values, predicted_values):
    squared_errors = []
    for actual, predicted in zip(actual_values, predicted_values):
        error = (actual - predicted) ** 2
        squared_errors.append(error)
    mse = sum(squared_errors) / len(actual_values)
    return mse

# Check if in the given string there are only digits
def onlyNbr(str):
    if (len(str) != 0):
        for i in str:
            if not i.isdigit():
                return False
        return True
    return (True)

def obtain_data():
    km = []
    price = []

    try:
        with open("data.csv", 'r') as file: # With to open and close
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if len(row) != 0 and onlyNbr(row[0]) is True and onlyNbr(row[1]) is True: # Skip the empty lines
                    km.append(int(row[0]))
                    price.append(int(row[1]))
    except Exception as e:
        print("Error: ", e)
    return km, price

def get_trained_thetas(filename):
    with open(filename, 'r') as file:
        theta0, theta1 = map(float, file.readline().split())
    return theta0, theta1

def hypothesis(theta0, theta1, mileage):
    value = float(theta0) + (float(theta1) * float(mileage))
    return value

def calculate_predicted_prices(theta0, theta1, km):
    predicted = []

    for x in km:
        predicted.append(hypothesis(theta0, theta1, x))
    return predicted

def calculate_R2(km, price):
    mean_km = sum(km) / len(km)
    mean_price = sum(price) / len(price)

    # Calculate the covariance
    covariance = sum((xx - mean_km) * (yy - mean_price) for xx, yy in zip(km, price)) / len(km)

    # Calculate the variance (o)
    sum_squared_diff = 0
    sum_squared_diff = sum((xx - mean_km) ** 2 for xx in km)
    variance_km = sum_squared_diff / len(km)

    #variance_km = sum((xx - mean_km) ** 2 for xx in km) / len(km)
    variance_price = sum((yy - mean_price) ** 2 for yy in price) / len(price)

    # Calculate R
    var = (variance_km ** 0.5 * variance_price ** 0.5)
    correlation_coefficient = covariance / var

    return correlation_coefficient ** 2


def main():
    if os.path.exists("data.csv") and os.path.exists("thetas.txt"):
        km, price = obtain_data()
        theta0, theta1 = get_trained_thetas("thetas.txt")
        predicted = calculate_predicted_prices(theta0, theta1, km)
        error = calculate_mean_square_error(price, predicted)
        R2 = calculate_R2(km, price)
        save_square_error(error, R2)
    else:
        print("Please, provide a data.csv file and train your model")

if __name__ == "__main__": 
    main()
