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