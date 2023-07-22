import sys
import  csv
import os.path

# estimatePrice(mileage) = theta0 + (theta1 * mileage)

def main():
    theta0 = 0.
    theta1 = 0.
    price = []
    km = []
    #while len(mileage) is 0:
   #     print("Enter the mileage: ")
    mileage = input("Enter the mileage: ")
    try:
        mileage = float(mileage)
        try:
            with open("data.csv", 'r') as csv_file :
      #      with open('file', 'r') as csv_file:
                value = csv_file.readlines()
                index = value[0].index('=')
        except Exception as e:
            print("Error: ", e)
        print("Price: ")
    except ValueError as e:
        print(e, "Enter the mileage: ")
        main()

if __name__ == "__main__":
    main()

#    if len(argv) == 0:
#        print("The result of the prediction which should be 0 since it has not gone through the learning phase")