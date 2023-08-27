import pandas as pd
from matplotlib import pyplot as plt
import csv
import os.path

def only_digit(str):
    for i in str:
        if not i.isdigit():
            return False
    return True

def obtain_data():
    km = []
    price = []

    try:
        with open("data.csv", 'r') as file: # With to open and close
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if len(row) != 0 and only_digit(row[0]) is True and only_digit(row[1]) is True: # Skip the empty lines
                    km.append(int(row[0]))
                    price.append(int(row[1]))
    except Exception as e:
        print("Error: ", e)
    return km, price

def hypothesis(theta0, theta1, x):
    return theta0 + (theta1 * x)

def get_trained_thetas(filename):
    with open(filename, 'r') as file:
        theta0, theta1 = map(float, file.readline().split())
    return theta0, theta1

def main():
    if os.path.exists("data.csv") and os.path.exists("thetas.txt"):
        km, price = obtain_data()
        theta0, theta1 = get_trained_thetas("thetas.txt")

        plt.scatter(km, price, label= "stars", color= "blue", marker= "*", s=30)
        prediction = [hypothesis(theta0, theta1, x) for x in km]
        plt.plot(km, prediction, label="Line", color="blue");

        plt.xlabel('Km')
        plt.ylabel('Price')
        plt.title('Plotting data into a graph!')
        plt.show()

    else:
        print("Please, provide a data.csv file and train your model")

if __name__ == "__main__":
    main()