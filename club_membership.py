from utils import *


def run_recreation_club():

    start = 1

    total_income = 0

    basic_count = 0
    premium_count = 0
    family_count = 0

    print(" ")
    print("*"*50, "Recreation Club Membership System", "*"*50)
    print(" ")

    while start != 0:

        try:

            print("Main menu")
            print("1. Register members")
            print("2. Show report and exit")

            op = int(input("Select a option: "))
            cs()

            if op == 1:

                members = int(input("How many members to register: "))
                cs()

                for i in range(members):

                    print("Member", i + 1)

                    name = input("Enter name: ")
                    age = int(input("Enter age: "))

                    print("Select membership plan")
                    print("1. Basic - 50000")
                    print("2. Premium - 90000")
                    print("3. Family - 130000")

                    plan = int(input("Select plan: "))

                    cs()

                    if age < 18:
                        print("Youth registration")

                    elif age >= 60:
                        print("Senior benefit")

                    if plan == 1:
                        price = 50000
                        basic_count += 1

                    elif plan == 2:
                        price = 90000
                        premium_count += 1

                    elif plan == 3:
                        price = 130000
                        family_count += 1

                    else:
                        print("Invalid plan")
                        p(3)
                        cs()
                        continue

                    total_income += price

                    print("Member registered:", name)
                    print("Plan price:", price)

                    p(3)
                    cs()

            elif op == 2:

                print("Club report")
                print("-"*50)

                print("Total income:", total_income)

                print("Basic plan:", basic_count)
                print("Premium plan:", premium_count)
                print("Family plan:", family_count)

                if basic_count > premium_count and basic_count > family_count:
                    print("Most sold plan: Basic")

                elif premium_count > basic_count and premium_count > family_count:
                    print("Most sold plan: Premium")

                elif family_count > basic_count and family_count > premium_count:
                    print("Most sold plan: Family")

                else:
                    print("Plans sold equally")

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