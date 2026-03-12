from utils import *


def run_sports_store_inventory():

    start = 1

    out_stock = 0
    low_stock = 0
    normal_stock = 0

    print(" ")
    print("*"*50, "Sports Store Inventory System", "*"*50)
    print(" ")

    while start != 0:

        try:

            print("Main menu")
            print("1. Register products")
            print("2. Show report and exit")

            op = int(input("Select a option: "))
            cs()

            if op == 1:

                for i in range(10):

                    print("Product", i + 1)

                    name = input("Enter product name: ")
                    quantity = int(input("Enter quantity available: "))

                    cs()

                    if quantity == 0:
                        print(name, "→ Out of stock")
                        out_stock += 1

                    elif quantity <= 5:
                        print(name, "→ Low stock")
                        low_stock += 1

                    else:
                        print(name, "→ Normal stock")
                        normal_stock += 1

                    p(3)
                    cs()

            elif op == 2:

                print("Inventory report")
                print("-"*50)

                print("Out of stock:", out_stock)
                print("Low stock:", low_stock)
                print("Normal stock:", normal_stock)

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