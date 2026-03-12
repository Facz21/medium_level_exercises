from utils import *

def run_gym_acces():

    start = 1
    
    print(" ") 
    print("*"*50, "Alpha Gym", "*"*50)
    print(" ") 
    
    


    while start != 0:

        try:
            print("Main menu")
            print("1. Enter new age")
            print("2. End process")
            op = int(input("Select a option: "))
            ext = 1
            cs()
            if op == 1:
                while ext != 0 : 
                    print("Welcome to age validation")
                    print("-"*50) 
                    age = int(input("Enter your age(Press O to leave): "))
                    if age == 0:
                        print("End process")
                        ext = 0
                    elif age < 0:
                        print("Enter a valid age ")
                        
                    elif age < 13:
                        print("You are still too young for the gym.")
                        
                    elif age >= 13 and age <= 17:
                        print("You can join the youth class.")
                        
                    elif age  >= 18  and age <= 59:
                        print("You can join the general class.")
                       
                    elif age  >= 60 and age <= 110:
                        print("You can join the senior class,")
                       
                    
                    
            if op == 2:
                print("Good bye :D")
                start = 0

        except ValueError:
            cs()
            print("Type a valid character (Intiger numbers)")
            p(5)
            cs()

