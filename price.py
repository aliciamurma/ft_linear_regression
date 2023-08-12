import sys
import csv
import os.path
import re
import pandas as pd
import matplotlib.pyplot as plt

# estimatePrice(mileage) = theta0 + (theta1 * mileage)
# with cierra el archivo automaticamente
# Una vez que el bloque de codigo finaliza, el archivo se cierra automaticamente

def isCorrectData(lenKm, lenPrice):
    if (lenKm != lenPrice):
        print("Error in datafile")
        sys.exit(-1)

def isCorrectRow():
    nRow = 0
    nCol = 0

    with open("data.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            nRow += 1
            if nRow == 1:  # La primera fila contiene los encabezados/columnas
                nCol = len(row)
    if (nRow != 2):
        print("Error in datafile")
        sys.exit(-1)

def getLenData():
    km = []
    price = []

    with open("data.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if len(row) >= 2: # Si hay mas de 2 columnas
                km.append(row[0])
                price.append(row[1])
    isCorrectData(len(km), len(price))
    return len(km)

def getTheta():
    theta0 = 0.
    theta1 = 0.
    i = 0

    if os.path.exists("data.csv"):
        with open("data.csv", 'r') as f:
            lines = f.readlines()
            print("i ", i)
            for row in lines:
                if i != 0:
                    theta0 = float(row[0])
                    theta1 = float(row[1])
                    break
                i += 1
    print("t0 ", theta0, "t1 ", theta1)
    return (theta0, theta1)

# Function to predict price based on mileage
def formula(theta0, theta1, mileage):
    value = float(theta0) + (float(theta1) * float(mileage))
    return value

def trainedThetas(filename):
    with open(filename, 'r') as file:
        theta0, theta1 = map(float, file.readline().split())
    return theta0, theta1

def onlyNbr(str):
    for i in str:
        if not i.isdigit():
            return False
    return True

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
