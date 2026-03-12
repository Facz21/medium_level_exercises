from utils import *


def run_ice_cream_clients():

    start = 1

    total_sold = 0
    total_clients = 0

    cone_count = 0
    cup_count = 0
    banana_count = 0

    print(" ")
    print("*"*50, "Ice Cream Shop System", "*"*50)
    print(" ")

    while start != 0:

        try:

            print("Main menu")
            print("1. Register client order")
            print("2. Show report and exit")

            op = int(input("Select a option: "))
            cs()

            if op == 1:

                print("Ice cream menu")
                print("-"*50)
                print("1. Cone - 3000")
                print("2. Cup - 4000")
                print("3. Banana Split - 9000")

                product = int(input("Select a product: "))
                quantity = int(input("Enter quantity: "))

                cs()

                if product == 1:

                    total = quantity * 3000
                    cone_count += quantity

                elif product == 2:

                    total = quantity * 4000
                    cup_count += quantity

                elif product == 3:

                    total = quantity * 9000
                    banana_count += quantity

                else:

                    print("Invalid product")
                    p(5)
                    cs()
                    continue

                print("Total to pay:", total)

                total_sold += total
                total_clients += 1

                p(5)
                cs()

            elif op == 2:

                print("Sales report")
                print("-"*50)

                print("Total sold:", total_sold)
                print("Clients attended:", total_clients)

                if cone_count > cup_count and cone_count > banana_count:
                    print("Most requested product: Cone")

                elif cup_count > cone_count and cup_count > banana_count:
                    print("Most requested product: Cup")

                elif banana_count > cone_count and banana_count > cup_count:
                    print("Most requested product: Banana Split")

                else:
                    print("Products requested equally")

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