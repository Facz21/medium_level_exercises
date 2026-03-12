from utils import *


def run_spa_services():

    start = 1

    print(" ")
    print("*"*50, "Spa Service System", "*"*50)
    print(" ")

    while start != 0:

        try:

            print("Main menu")
            print("1. Request service")
            print("2. End process")

            op = int(input("Select a option: "))
            cs()

            if op == 1:

                print("Select a service")
                print("-"*50)
                print("1. Massage")
                print("2. Facial")
                print("3. Manicure")

                service = int(input("Select a option: "))
                cs()

                if service == 1:
                    print("Massage service scheduled")

                elif service == 2:
                    print("Facial service scheduled")

                elif service == 3:
                    print("Manicure service scheduled")

                else:
                    print("Service not available")

                p(5)
                cs()

            elif op == 2:

                print("Leaving spa system...")
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