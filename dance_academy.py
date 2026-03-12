from utils import *


def run_dance_academy():

    start = 1

    print(" ")
    print("*"*50, "Dance Academy Attendance", "*"*50)
    print(" ")

    while start != 0:

        try:

            print("Main menu")
            print("1. Check attendance")
            print("2. End process")

            op = int(input("Select a option: "))
            cs()

            if op == 1:

                print("Attendance evaluation")
                print("-"*50)

                classes = int(input("Enter number of classes attended: "))
                cs()

                if classes < 0:
                    print("Enter a valid number")

                elif classes < 5:
                    print("Low attendance")

                elif classes <= 8:
                    print("Medium attendance")

                else:
                    print("High attendance")

                p(5)
                cs()

            elif op == 2:

                print("Leaving academy system...")
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