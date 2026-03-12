from utils import *


def run_parking_control():

    start = 1

    total_income = 0
    car_count = 0
    moto_count = 0

    max_payment = 0
    max_plate = ""

    print(" ")
    print("*"*50, "Parking Control System", "*"*50)
    print(" ")

    while start != 0:

        try:

            print("Main menu")
            print("1. Register vehicles")
            print("2. Exit and show report")

            op = int(input("Select a option: "))
            cs()

            if op == 1:

                for i in range(8):

                    print("Vehicle", i + 1)

                    plate = input("Enter plate: ")

                    print("Vehicle type")
                    print("1. Car")
                    print("2. Motorcycle")

                    vtype = int(input("Select type: "))

                    hours = int(input("Hours parked: "))

                    cs()

                    if vtype == 1:

                        total = hours * 4000
                        car_count += 1

                    elif vtype == 2:

                        total = hours * 2000
                        moto_count += 1

                    else:

                        print("Invalid vehicle type")
                        p(3)
                        cs()
                        continue

                    print("Vehicle plate:", plate)
                    print("Total to pay:", total)

                    total_income += total

                    if total > max_payment:
                        max_payment = total
                        max_plate = plate

                    p(4)
                    cs()

            elif op == 2:

                print("Parking report")
                print("-"*50)

                print("Total income:", total_income)
                print("Cars registered:", car_count)
                print("Motorcycles registered:", moto_count)
                print("Vehicle with highest payment:", max_plate)
                print("Highest payment:", max_payment)

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