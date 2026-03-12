#Ice Cream shop:

#We call the functions in utils.py
from utils import*
 
# 
def run_ice_cream_shop():

    start = 1

    vanilla = 0 
    chocolate = 0
    strawberry = 0
    
    print(" ") 
    print("*"*50,"Magic Ice Cream","*"*50)
    print(" ") 
    print("Welcome dear user") 
    print(" ")
    
    while start != 0:

        try:
            p(0.5)
            vop = [1, 2]
            print("Main menu")
            p(0.5)
            print("1. New order")
            p(0.5)
            print("2. End process")
            p(0.5)
            op = int(input("Select a option: "))
            vanilla = 0 
            chocolate = 0
            strawberry = 0
            cs()
            if op in vop:
                
                if op == 1:
                    print("Welcome to flavor select")
                    print("-"*50)
                    p(0.5)
                    flavor_op = 0
                    while flavor_op != 4:
                        try:
                            print("Choose a flavor to serve")
                            print(" ")
                            p(0.5)
                            print("1. Vanilla")
                            p(0.5)
                            print("2. Chocolate")
                            p(0.5)
                            print("3. Strawberry")
                            p(0.5)
                            print("4. End order")
                            p(0.5)
                            print(" ")
                            flavor_op = int(input("Select a option: "))
                            cs()
                            if flavor_op == 1:
                                vanilla += 1
                                l("Preparing vanilla ice cream")
                                print("Vanilla served!")
                                p(1)
                                cs()
                            elif flavor_op == 2:
                                chocolate += 1 
                                l("Preparing chocolate ice cream")
                                print("Chocolate served!")
                                p(1)
                                cs()
                            elif flavor_op == 3:
                                strawberry += 1
                                l("Preparing strawberry ice cream")
                                print("Strawberry served!")
                                p(1)
                                cs()
                            elif flavor_op ==4:
                                s()
                                cs()
                                print("Total serves: \n"
                                " " 
                                f"Vanilla: {vanilla} \n"
                                f"Chocolate: {chocolate} \n"
                                f"Strawberry: {strawberry}")
                                p(5)
                                cs()

                            else:
                                print("Enter a valid option (Number escale 1 to 4.)")
                                p()
                                cs()   

                        except ValueError:
                            cs()
                            print("Type a valid number")   
                            p(5)
                            cs()        

                elif op == 2:
                    print("Leaving the program")
                    start = 0



            else: 
                cs()
                print("Enter a valid option (Number escale 1 to 2.)")
                p(5)
                cs()

        except ValueError:
            cs()
            print("Type a valid character (Numbers at 1 to 2)")
            p(5)
            cs()       

