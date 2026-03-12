#We call the functions in utils.py
from utils import *


def run_parking_lot():

    start = 1

    print(" ")
    print("*"*50, "Parking Lot System", "*"*50)
    print(" ")

    while start != 0:

        try:

            print("Main menu")
            print("1. Calculate parking cost")
            print("2. End process")

            op = int(input("Select a option: "))
            cs()

            if op == 1:

                print("Parking time calculator")
                print("-"*50)

                hours = int(input("Enter number of hours: "))

                cs()

                if hours <= 0:

                    print("Enter a valid number of hours")

                elif hours == 1:

                    total = 5000
                    print(f"Total to pay: {total}")

                else:

                    total = 5000 + (hours - 1) * 3000
                    print(f"Total to pay: {total}")

                p(5)
                cs()

            elif op == 2:

                print("Leaving parking system...")
                start = 0

            else:

                print("Enter a valid option (1 or 2)")
                p(5)
                cs()

        except ValueError:

            cs()
            print("Type a valid number")
            p(5)
            cs()