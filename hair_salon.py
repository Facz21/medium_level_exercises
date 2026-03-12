from utils import *


def run_hair_salon():

    start = 1

    print(" ")
    print("*"*50, "Hair Salon Schedule", "*"*50)
    print(" ")

    while start != 0:

        try:

            print("Main menu")
            print("1. Check client arrival")
            print("2. End process")

            op = int(input("Select a option: "))
            cs()

            if op == 1:

                print("Client arrival time")
                print("-"*50)

                hour = int(input("Enter arrival hour (0 - 23): "))

                cs()

                if hour < 0 or hour > 23:
                    print("Enter a valid hour")

                elif 6 <= hour <= 11:
                    print("Morning shift")

                elif 12 <= hour <= 17:
                    print("Afternoon shift")

                elif 18 <= hour <= 22:
                    print("Night shift")

                else:
                    print("Out of service hours")

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