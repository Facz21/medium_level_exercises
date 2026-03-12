#We call the functions in utils.py
from utils import *


def run_cafeteria():

    start = 1

    coffee_price = 4000
    tea_price = 3500
    juice_price = 5000

    print(" ")
    print("*"*50, "Magic Cafeteria", "*"*50)
    print(" ")

    while start != 0:

        try:

            print("Main menu")
            print("1. New order")
            print("2. End process")

            op = int(input("Select a option: "))
            cs()

            if op == 1:

                print("Welcome to beverage order")
                print("-"*50)

                print("Menu")
                print("1. Coffee - 4000")
                print("2. Tea - 3500")
                print("3. Juice - 5000")

                drink = int(input("Select your drink: "))

                qty = int(input("Enter quantity: "))

                cs()

                if drink == 1:

                    total = coffee_price * qty

                    print("Preparing coffee...")
                    print(f"Total to pay: {total}")

                elif drink == 2:

                    total = tea_price * qty

                    print("Preparing tea...")
                    print(f"Total to pay: {total}")

                elif drink == 3:

                    total = juice_price * qty

                    print("Preparing juice...")
                    print(f"Total to pay: {total}")

                else:

                    print("Enter a valid option")

                p(5)
                cs()

            elif op == 2:

                print("Leaving the cafeteria...")
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