from utils import *


def run_gym_performance():

    start = 1

    low_commitment = 0
    medium_commitment = 0
    high_commitment = 0

    print(" ")
    print("*"*50, "Gym Weekly Performance", "*"*50)
    print(" ")

    while start != 0:

        try:

            print("Main menu")
            print("1. Register weekly performance")
            print("2. Exit and show report")

            op = int(input("Select a option: "))
            cs()

            if op == 1:

                print("Registering 5 gym members")
                print("-"*50)

                for i in range(5):

                    print("Person", i + 1)

                    name = input("Enter name: ")
                    days = int(input("Days attended this week: "))
                    minutes = int(input("Average minutes trained per day: "))

                    cs()

                    if days < 3:
                        print(name, "→ Low commitment")
                        low_commitment += 1

                    elif days <= 4:
                        print(name, "→ Medium commitment")
                        medium_commitment += 1

                    else:
                        print(name, "→ High commitment")
                        high_commitment += 1

                    p(3)

                cs()

            elif op == 2:

                print("Weekly report")
                print("-"*50)

                print("Low commitment:", low_commitment)
                print("Medium commitment:", medium_commitment)
                print("High commitment:", high_commitment)

                start = 0

            else:

                print("Enter a valid option")
                p(5)
                cs()

        except ValueError:

            cs()
            print("Type a valid number")
            p(5)
            cs()
