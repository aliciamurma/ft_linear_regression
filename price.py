import sys
import csv
import os.path
import re
import pandas as pd

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

def getTethas():
    try:
        if os.path.exists("data.csv"):
            with open("data.csv", 'r') as f:
                lines = f.readlines()
                
    except Exception as e:
        print("Error 1: ", e)

def main():
    theta0 = 0.
    theta1 = 0.
    dataLen = getLenData() -1

    mileage = input("Enter the mileage: ")
    while ((mileage <= 0)):
        mileage = input("Enter the mileage: ")

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

if __name__ == "__main__":
    main()
