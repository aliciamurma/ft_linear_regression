import sys
import csv
import os.path
import re
import pandas as pd
import matplotlib.pyplot as plt

# estimatePrice(mileage) = theta0 + (theta1 * mileage)
# with cierra el archivo automaticamente
# Una vez que el bloque de codigo finaliza, el archivo se cierra automaticamente

# Predict price based on mileage
def formula(theta0, theta1, mileage):
    value = float(theta0) + (float(theta1) * float(mileage))
    return value

def trainedThetas(filename):
    with open(filename, 'r') as file:
        theta0, theta1 = map(float, file.readline().split())
    return theta0, theta1

# Check if the given string only contains positive numbers
# In a linear regression you can use negative numbers, but in that case, you cannot have a negative km or negative price
def onlyNbr(str):
    for i in str:
        if not i.isdigit():
            return False
    return True

# Enter a mileage and check it is correct
def enterMileage():
    mileage_str = input("Enter the mileage: ")
    while (len(mileage_str) == 0) or (onlyNbr(mileage_str) is False):
        mileage_str = input("Enter a positive numeric mileage: ")
    mileage = float(mileage_str)
    while (len(mileage_str) == 0) or (onlyNbr(mileage_str) is False):
        mileage_str = input("Enter a positive numeric mileage: ")
    mileage = float(mileage_str)
    print("Thanks!")
    return (mileage)

def main():
    theta0 = 0.0
    theta1 = 0.0
    price = []

    mileage = enterMileage()
    if os.path.exists("thetas.txt"):
        theta0, theta1 = trainedThetas("thetas.txt")
        price = formula(theta0, theta1, mileage)
    else:
        price = 0
    if price < 0:
        print("Error in price")
    else:
        print("ESTIMATED PRICE: ", price)

if __name__ == "__main__":
    main()
