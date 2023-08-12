import sys
import math

def formula(theta0, theta1, mileage):
    value = theta0 + (theta1 * mileage)
    return value

def sumTheta0(theta0, theta1, km, price, m):
    for i in range(0, m):
        value = value + formula(theta0, theta1, km[i]) - price[i]
    return value

def sumTheta1(theta0, theta1, km, price, m):
    for i in range(0, m):
        value = value + (formula(theta0, theta1, km[i]) - price[i]) * km[i]
    return value

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