from utils import *


def run_sport_store():

    start = 1

    print(" ")
    print("*"*50, "Sport Store Price Counter", "*"*50)
    print(" ")

    while start != 0:

        try:

            print("Main menu")
            print("1. Register product prices")
            print("2. End process")

            op = int(input("Select a option: "))
            cs()

            if op == 1:

                print("Product price registration")
                print("-"*50)

                count = 0
                i = 1

                while i <= 6:

                    price = int(input(f"Enter price of product {i}: "))

                    if price > 100000:
                        count += 1

                    i += 1

                cs()

                print(f"Products over 100000: {count}")

                p(5)
                cs()

            elif op == 2:

                print("Leaving system...")
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