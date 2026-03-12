from utils import *


def run_cinema_control():

    start = 1

    total_people = 0
    kids = 0
    adults = 0
    seniors = 0

    print(" ")
    print("*"*50, "Cinema Room Control", "*"*50)
    print(" ")

    while start != 0:

        try:

            print("Main menu")
            print("1. Start room control")
            print("2. Exit")

            op = int(input("Select a option: "))
            cs()

            if op == 1:

                capacity = int(input("Enter total room capacity: "))
                cs()

                for i in range(capacity):

                    print("Person", i + 1)

                    age = int(input("Enter age: "))

                    if age < 18:
                        kids += 1

                    elif age < 60:
                        adults += 1

                    else:
                        seniors += 1

                    total_people += 1

                    print("Person registered")
                    p(2)
                    cs()

                print("Room registration completed")

            elif op == 2:

                print("Cinema report")
                print("-"*50)

                print("Total people:", total_people)
                print("Kids:", kids)
                print("Adults:", adults)
                print("Seniors:", seniors)

                if total_people >= capacity:
                    print("The room is full")
                else:
                    print("The room is not full")

                start = 0

            else:

                print("Enter a valid option")
                p(4)
                cs()

        except ValueError:

            cs()
            print("Type a valid number")
            p(4)
            cs()