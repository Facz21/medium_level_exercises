#We call the functions in utils.py
from utils import *


def run_pet_shop():

    start = 1

    print(" ")
    print("*"*50, "Pet Food Recommendation", "*"*50)
    print(" ")

    while start != 0:

        try:

            print("Main menu")
            print("1. New consultation")
            print("2. End process")

            op = int(input("Select a option: "))
            cs()

            if op == 1:

                print("Pet type consultation")
                print("-"*50)

                print("Select the type of pet")
                print("1. Dog")
                print("2. Cat")
                print("3. Rabbit")

                pet = int(input("Select a option: "))

                cs()

                if pet == 1:
                    print("Recommended food: Premium dog kibble")

                elif pet == 2:
                    print("Recommended food: Fish based cat food")

                elif pet == 3:
                    print("Recommended food: Fresh vegetables and hay")

                else:
                    print("Enter a valid option (1 to 3)")

                p(5)
                cs()

            elif op == 2:

                print("Leaving pet shop system...")
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
