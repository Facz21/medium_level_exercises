from utils import *


def run_cafeteria_discount():

    start = 1
    total_day = 0

    print(" ")
    print("*"*50, "Cafeteria Sales System", "*"*50)
    print(" ")

    while start != 0:

        try:

            print("Main menu")
            print("1. Register order")
            print("2. Show total and exit")

            op = int(input("Select a option: "))
            cs()

            if op == 1:

                print("Cafeteria menu")
                print("-"*50)
                print("1. Coffee - 4000")
                print("2. Cappuccino - 7000")
                print("3. Cake - 6000")

                product = int(input("Select a product: "))
                quantity = int(input("Enter quantity: "))

                cs()

                if product == 1:
                    total = quantity * 4000

                elif product == 2:
                    total = quantity * 7000

                elif product == 3:
                    total = quantity * 6000

                else:
                    print("Invalid product")
                    p(4)
                    cs()
                    continue

                if total > 20000:
                    discount = total * 0.10
                    final_total = total - discount
                    print("Discount applied: 10%")
                else:
                    final_total = total

                print("Total to pay:", final_total)

                total_day += final_total

                p(5)
                cs()

            elif op == 2:

                print("Daily sales report")
                print("-"*50)
                print("Total accumulated:", total_day)

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