import pandas as pd
from matplotlib import pyplot as plt
import csv

def onlyNbr(str):
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
                if len(row) != 0 and onlyNbr(row[0]) is True and onlyNbr(row[1]) is True: # Skip the empty lines
                    km.append(int(row[0]))
                    price.append(int(row[1]))
    except Exception as e:
        print("Error: ", e)
    return km, price

def main():
    km, price = obtain_data()
    plt.scatter(km, price, label= "stars", color= "blue", marker= "*", s=30)
#    plt.plot(km, price) if we use that line and not the previous one, will appear lines instead of "*"
    plt.xlabel('Km')
    plt.ylabel('Price')
    plt.title('Plotting data into a graph!')
    plt.show()

if __name__ == "__main__":
    main()