#We call the functions in utils.py
from utils import *


def run_cinema_ticket():

    start = 1

    print(" ")
    print("*"*50, "Cinema Ticket System", "*"*50)
    print(" ")

    while start != 0:

        try:

            print("Main menu")
            print("1. New client")
            print("2. End process")

            op = int(input("Select a option: "))
            cs()

            if op == 1:

                print("Cinema ticket calculator")
                print("-"*50)

                age = int(input("Enter client age: "))

                cs()

                if age < 0:

                    print("Enter a valid age")

                elif age < 12:

                    price = 8000
                    print("Child ticket")
                    print(f"Total to pay: {price}")

                elif age <= 59:

                    price = 12000
                    print("Adult ticket")
                    print(f"Total to pay: {price}")

                else:

                    price = 9000
                    print("Senior ticket")
                    print(f"Total to pay: {price}")

                p(5)
                cs()

            elif op == 2:

                print("Leaving cinema system...")
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