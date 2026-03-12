from utils import *


def run_hair_salon():

    start = 1

    total_day = 0

    cut_count = 0
    brushing_count = 0
    dye_count = 0

    print(" ")
    print("*"*50, "Hair Salon Agenda System", "*"*50)
    print(" ")

    while start != 0:

        try:

            print("Main menu")
            print("1. Register clients")
            print("2. Show report and exit")

            op = int(input("Select a option: "))
            cs()

            if op == 1:

                for i in range(7):

                    print("Client", i + 1)

                    name = input("Enter client name: ")

                    print("Service requested")
                    print("1. Haircut")
                    print("2. Brushing")
                    print("3. Hair dye")

                    service = int(input("Select service: "))
                    value = int(input("Enter value paid: "))

                    cs()

                    if service == 1:
                        cut_count += 1

                    elif service == 2:
                        brushing_count += 1

                    elif service == 3:
                        dye_count += 1

                    else:
                        print("Invalid service")
                        p(3)
                        cs()
                        continue

                    total_day += value

                    print("Client registered:", name)

                    p(3)
                    cs()

            elif op == 2:

                print("Daily report")
                print("-"*50)

                print("Total earned:", total_day)

                print("Haircuts:", cut_count)
                print("Brushing:", brushing_count)
                print("Hair dye:", dye_count)

                if cut_count > brushing_count and cut_count > dye_count:
                    print("Most requested service: Haircut")

                elif brushing_count > cut_count and brushing_count > dye_count:
                    print("Most requested service: Brushing")

                elif dye_count > cut_count and dye_count > brushing_count:
                    print("Most requested service: Hair dye")

                else:
                    print("Services requested equally")

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
