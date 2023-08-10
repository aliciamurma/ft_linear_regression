import sys
import csv
import os.path
import re
import pandas as pd
import numpy as np
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

def getKm():
    km = []
    i = 0

    for line in open("data.csv").readlines():
        if (len(line) != 0 and len(line) != 1):
            index = line.index(',')
            tmp = line[:index]
            print("tmp: ", tmp)
            if i != 0:
                try:
                    tmp = float(tmp) / 1000
                except Exception as e:
                    print("Error 1: ", e)
            km.append(tmp)
        i += 1
    km = km[1:]
    print(km)

def getPrice():
    price = []
    i = 0

    for line in open("data.csv").readlines():
        if (len(line) != 0 and len(line) != 1):
            index = line.index(',')
            tmp = line[index +1: -1]
            print("tmp: ", tmp)
            if i != 0:
                try:
                    tmp = float(tmp) / 1000
                except Exception as e:
                    print("Error 1: ", e)
            price.append(tmp)
        i += 1
    price = price[1:]
    print(price)

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

def main():
    theta0 = 0.0
    theta1 = 0.0
    price = []

    mileage = input("Enter the mileage: ")
    while (int(mileage) <= 0):
        mileage = input("Enter the mileage: ")
    
    theta0, theta1 = getTheta()
    price = formula(theta0, theta1, mileage)
    if price < 0:
        print("Error in price")
    else:
        print("ESTIMATED PRICE: ", price)

    file = "data.csv"
    data = pd.read_csv(file)
    data.head()
    fig = plt.figure(figsize=(14,14))

"""
    dataframe.shape
    dataframe.head()
    dataframe.describe()
"""

"""
    try:
        mileage = float(mileage)
        try:
            if os.path.exists("data.csv"):
                with open("data.csv", 'r') as f:
                    lines = f.readlines()
                    theta0 = lines[1][0]
                    theta1 = lines[1][1]
        except Exception as e:
            print("Error 1: ", e)
        
        print("THETA0", theta0)
        print("THETA1", theta1)
        print("mileage", mileage)

        price = float(theta0) + (float(theta1) * float(mileage))
        
        #print("Price: ")
        #print(hypothesis(float(theta0), float(theta1), mileage))
    #    price = theta0 + (theta1 * float(mileage)) # equivale a la funcion y = mx + b
        print(price)
    except ValueError as e:
        print(e, "Enter the mileage: ")
        main()
"""

if __name__ == "__main__":
    main()
