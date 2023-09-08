import sys
import csv
import os.path
import re
import pandas as pd
import matplotlib.pyplot as plt

# tmp0 = learningRate * 1/m suma(estimatePrice(mileage[i]) - price[i])
# tmp1 = learningRate * 1/m suma(estimatePrice(mileage[i]) - price[i]) * mileage[i]
# tmpTheta0 = learningRate * 1/m * Σ(estimatePrice(mileage[i] - price[i])) tmpTheta1 = learningRate * 1/m * Σ(estimatePrice(mileage[i] - price[i])) * mileage[i]

# Check if we have the same n for km and for price
def isCorrectData(lenKm, lenPrice):
    if lenKm != lenPrice or lenKm < 3:
        print("Error in datafile lenght")
        sys.exit(-1)

# Check if there is 2 rows and there is not more data than necessary
def isCorrectRow():
    nRow = 0
    nCol = 0

    with open("data.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            nRow += 1
            nCol = len(row)
            if (nCol != 2 and nCol != 0):
                print("Error in number of columns in the datafile")
                sys.exit(-1)

# Get the lenght of the data
def getLenData():
    km = []
    price = []

    with open("data.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if len(row) >= 2: # Si hay mas de 2 filas
                km.append(row[0])
                price.append(row[1])

    return len(km), len(price)

def checkCorrectLenData():
    km = []
    price = []
    i = 0

    with open("data.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if len(row) >= 2:
                if len(row) > 0:
                    km_value = row[0]
                    price_value = row[1]

                if len(km_value) == 0:
                    print("Error, incorrect km length")
                    sys.exit()
                if len(price_value) == 0:
                    print("Error, incorrect price length")
                    sys.exit()

                km.append(km_value)
                price.append(price_value)
                
            i += 1

# Check if in the given string there are only digits
def onlyNbr(str):
    if (len(str) != 0):
        for i in str:
            if not i.isdigit():
                return False
        return True
    return (True)

# Check if in the dataset file there are numbers in km and price
def checkNumbers():
    i = 0

    with open("data.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if i > 0:
                if (len(row) != 0 and (onlyNbr(row[0]) is False or onlyNbr(row[1]) is False)):
                    print("Error in datafile: not numeric character found")
                    sys.exit(-1)
            if (len(row) != 0):
                i += 1

# Check there is a header
def checkHeader():
    i = 0

    with open("data.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if i == 0:
                if (len(row) != 0 and (onlyNbr(row[0]) is True and onlyNbr(row[1]) is True)):
                    print("Write in the first line of your csv file: km,price")
                    sys.exit(-1)
            if (len(row) != 0):
                i += 1

# Check if the file is empty
def is_empty_file(file):
    if os.path.getsize(file) == 0:
        print("The file is empty!")
        sys.exit(-1)

# Check all the errors
def check_errors():
    is_empty_file("data.csv")
    checkHeader()
    checkCorrectLenData() # Check if there is any empty km or price (e.i.: ,3600)
    lenkm, lenPrice = getLenData() # Obtain the lenght of both columns
    isCorrectData(lenkm, lenPrice) # Check if there is the same number of kms than prices
    isCorrectRow() # Tenemos 2 columnas solamente
    checkNumbers() # Check if there are only numbers

def estimated_price(mileage, theta0, theta1):
    return theta0 + (theta1 * mileage)

# Update the thetas. Given formulas in the subject
def get_thetas(mileage, price, theta0, theta1, learningRate):
    m = len(mileage)
    temp0 = 0
    temp1 = 0

    temp0 = sum(estimated_price(mileage[i], theta0, theta1) - price[i] for i in range(m))
    temp1 = sum((estimated_price(mileage[i], theta0, theta1) - price[i]) * mileage[i] for i in range(m))

    tmp_theta0 = learningRate * (1/m) * temp0
    tmp_theta1 = learningRate * (1/m) * temp1

    return tmp_theta0, tmp_theta1

# Gives the error between the predicted prices based on the current thetas and the actual prices
def get_error(theta0, theta1, price, mileage):
    error = 0
    for i in range(len(mileage)): # Start the loop for mileage
        predictedPrice = theta0 + (theta1 * mileage[i]) # Calculate the price by linear regression
        # Calculate the standard desviation
        error += (predictedPrice - price[i]) ** 2 # Difference between the predicted price and the actual price
    error /= (2 * len(mileage)) # Divides the accumulative error by twice the number of data points 
    # The 2 * len(mileage) is to normalize the error
    return error

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

# Before, we have normalized the mileage, so now we have to unnormalized theta values
# We need the min and max values of mileage, bc we have normalized it with them
def calculate_real_thetas(theta0, theta1, max, min):
    real_theta0 = theta0 - theta1 * min / (max - min)
    real_theta1 = theta1 / (max - min)
    return real_theta0, real_theta1

def training_loop(normalized):
    tolerance = 0.0001
    iterations = 10000000 # The loop can stop before
    theta0 =  0.0 # Always start on 0
    theta1 =  0.0 # Always start on 0
    prev_cost = float('inf')  # Initialize with a large value

    try:
        mileage, price = obtain_data()

        for i in range(iterations):
            temp_theta0, temp_theta1 = get_thetas(normalized, price, theta0, theta1, 0.001)
            theta0 -= temp_theta0
            theta1 -= temp_theta1

            # Monitor the error of the linear regression until it be lower than 0.0001
            current_cost = get_error(theta0, theta1, price, normalized)
            cost_difference = abs(prev_cost - current_cost)
            prev_cost = current_cost
            if cost_difference < tolerance:
                break

    except Exception as e:
        print("Error: ", e)
    return theta0, theta1

def train_model():
    try:
        mileage, price = obtain_data()
        if len(mileage) < 2:
            print("Please, provide a set of numbers in the data.csv file.")
            sys.exit(-1)

        # Normalize mileage data (optional but in our case necessary bc the numbers are so high)
        max_mileage = max(mileage) # The highest mileage value in the dataset
        min_mileage = min(mileage) # The lowest mileage value in the dataset
        normalized_mileage = [(x - min_mileage) / (max_mileage - min_mileage) for x in mileage] # Normalization
        # The formula scales the mileage value 0-1 --> 0 minimum mileage // 1 maximum mileage

        # Obtain the thetas from the trained loop
        theta0, theta1 = training_loop(normalized_mileage)
        # Reverse normalization
        real_theta0, real_theta1 = calculate_real_thetas(theta0, theta1, max_mileage, min_mileage)

        with open('thetas.txt', 'w') as file:
            file.write(f"{real_theta0} {real_theta1}\n")
        print("Trained!")

    except Exception as e:
        print("Error: ", e)

def main():
    if os.path.exists("data.csv"): # Only if the file exists we can train our model
        print("Checking errors...") 
        check_errors()
        print("Training...")
        train_model()
    else:
        print("Please, provide a data.csv file")

if __name__ == "__main__": 
    main()
