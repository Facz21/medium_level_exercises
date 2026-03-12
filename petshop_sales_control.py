from utils import *


def run_petshop_sales():

    start = 1

    food_sales = 0
    toy_sales = 0
    accessory_sales = 0

    print(" ")
    print("*"*50, "Pet Shop Sales System", "*"*50)
    print(" ")

    while start != 0:

        try:

            print("Main menu")
            print("1. Register sales")
            print("2. Show report and exit")

            op = int(input("Select a option: "))
            cs()

            if op == 1:

                for i in range(10):

                    print("Sale", i + 1)

                    print("Category")
                    print("1. Food")
                    print("2. Toy")
                    print("3. Accessory")

                    category = int(input("Select category: "))
                    value = int(input("Enter sale value: "))

                    cs()

                    if category == 1:
                        food_sales += value

                    elif category == 2:
                        toy_sales += value

                    elif category == 3:
                        accessory_sales += value

                    else:
                        print("Invalid category")
                        p(3)
                        cs()
                        continue

                    print("Sale registered")
                    p(2)
                    cs()

            elif op == 2:

                print("Sales report")
                print("-"*50)

                print("Food sales:", food_sales)
                print("Toy sales:", toy_sales)
                print("Accessory sales:", accessory_sales)

                if food_sales > toy_sales and food_sales > accessory_sales:
                    print("Category with highest income: Food")

                elif toy_sales > food_sales and toy_sales > accessory_sales:
                    print("Category with highest income: Toy")

                elif accessory_sales > food_sales and accessory_sales > toy_sales:
                    print("Category with highest income: Accessory")

                else:
                    print("Categories generated similar income")

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