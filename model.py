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
    if (lenKm != lenPrice):
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
            if len(row) >= 2: # Si hay mas de 2 filas
                km.append(row[0])
                price.append(row[1])
                if len(km[i]) == 0:
                    print("Error, incorrect km lenght")
                    sys.exit()
                if len(price[i]) == 0:
                    print("Error, incorrect price lenght")
                    sys.exit()
                i += 1

def onlyNbr(str):
    if (len(str) != 0):
        for i in str:
            if not i.isdigit() and i != ",":
                return False
        return True
    return (True)

def checkNumbers():
    with open("data.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header
        for row in csv_reader:
            if (len(row) != 0 and (onlyNbr(row[0]) is False or onlyNbr(row[1]) is False)):
                print("Error in datafile: not numeric character found")
                sys.exit(-1)

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

def is_empty_file(file):
    return os.path.getsize(file) == 0

def checkErrors():
    if is_empty_file("data.csv"):
        print("The file is empty!")
        sys.exit(-1)
    checkHeader()
    lenkm, lenPrice = getLenData() # Obtain the lenght of both columns
    checkCorrectLenData() # Check if there is any empty km or price (e.i.: ,3600)
    isCorrectData(lenkm, lenPrice) # Check if there is the same number of kms than prices
    isCorrectRow() # Tenemos 2 columnas solamente
    checkNumbers() # Check if there are only numbers

# Update the thetas. Given formulas in the subject
def get_thetas(mileage, price, theta0, theta1, learningRate):
    temp0 = 0
    temp1 = 0
    for i in range(len(mileage)):
        temp0 += theta0 + theta1 * mileage[i] - price[i]
        temp1 += (theta0 + theta1 * mileage[i] - price[i]) * mileage[i]
    theta0 -= (learningRate * temp0) / len(mileage) # From the formula of linear regression, obtain the two variables
    theta1 -= (learningRate * temp1) / len(mileage)
    return theta0, theta1

# Calculate the standard desviation (error)
def get_error(theta0, theta1, price, mileage):
    error = 0
    for i in range(len(mileage)): # Start the loop for mileage
        predictedPrice = theta0 + (theta1 * mileage[i]) # Calculate the price by linear regression
        # Calculate the standard desviation
        error += (predictedPrice - price[i]) ** 2 # Difference between the predicted price and the actual price
    error /= (2 * len(mileage)) # Divides the accumulative error by twice the number of data points 
    # The 2 * len(mileage) is to normalize the error
    return error


def trainModel():
    price = []
    mileage = []
    theta0 =  0.0 # Always start on 0
    theta1 =  0.0 # Always start on 0
    iterations = 1000 # The nbr of iterations will be 1000, we can change it if it is required
    learningRate = 0.001
    try:
        with open("data.csv", 'r') as file: # With to open and close
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header
            for row in csv_reader:
                if len(row) != 0: # Skip the empty lines
                    price.append(float(row[0])) # Cast km to float
                    mileage.append(float(row[1])) # Cast price to float
        if len(mileage) < 2:
            print("Please, provide a set of numbers in the data.csv file.")
            sys.exit(-1)
        # Normalize mileage data (optional but in our case necessary bc the numbers are so high)
        max_mileage = max(mileage) # The highest mileage value in the dataset
        min_mileage = min(mileage) # The lowest mileage value in the dataset
        normalized_mileage = [(x - min_mileage) / (max_mileage - min_mileage) for x in mileage] # Normalization
        # The formula scales the mileage value 0-1 --> 0 minimum mileage // 1 maximum mileage
        
        # Training loop
        for i in range(iterations):
            theta0, theta1 = get_thetas(normalized_mileage, price, theta0, theta1, learningRate)
            error = get_error(theta0, theta1, price, normalized_mileage)
        with open('thetas.txt', 'w') as file:
            file.write(f"{theta0} {theta1}\n")
        print("Trained!")

    except Exception as e:
        print("Error: ", e)

def main():
    if os.path.exists("data.csv"): # Only if the file exists we can train our model
        print("Checking errors...")
        checkErrors()
        print("Training...")
        trainModel()
    else:
        print("Please, provide a data.csv file")

if __name__ == "__main__": 
    main()
