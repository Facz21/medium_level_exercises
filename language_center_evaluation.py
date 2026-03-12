from utils import *


def run_language_center():

    start = 1

    total_average = 0
    student_count = 0

    low_level = 0
    medium_level = 0
    high_level = 0

    best_average = 0
    best_student = ""

    print(" ")
    print("*"*50, "Language Center Evaluation", "*"*50)
    print(" ")

    while start != 0:

        try:

            print("Main menu")
            print("1. Register students")
            print("2. Show report and exit")

            op = int(input("Select a option: "))
            cs()

            if op == 1:

                students = int(input("How many students to register: "))
                cs()

                for i in range(students):

                    print("Student", i + 1)

                    name = input("Enter name: ")

                    speaking = int(input("Speaking score: "))
                    listening = int(input("Listening score: "))
                    reading = int(input("Reading score: "))

                    average = (speaking + listening + reading) / 3

                    cs()

                    print("Average:", average)

                    if average < 60:
                        print("Level: Low")
                        low_level += 1

                    elif average <= 79:
                        print("Level: Medium")
                        medium_level += 1

                    else:
                        print("Level: High")
                        high_level += 1

                    total_average += average
                    student_count += 1

                    if average > best_average:
                        best_average = average
                        best_student = name

                    p(3)
                    cs()

            elif op == 2:

                print("Course report")
                print("-"*50)

                if student_count > 0:
                    group_average = total_average / student_count
                else:
                    group_average = 0

                print("Group average:", group_average)
                print("Best student:", best_student)
                print("Best average:", best_average)

                print("Low level:", low_level)
                print("Medium level:", medium_level)
                print("High level:", high_level)

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