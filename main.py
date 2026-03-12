from gym_acces import run_gym_acces as rg
from ice_cream_shop import run_ice_cream_shop as ri
from magic_cafeteria import run_cafeteria as rc
from cinema_ticket_system import run_cinema_ticket as rct


def main():

    start = 1

    while start != 0 :

        print("\nMAIN MENU")
        print("-"*40)
        print("1. Age Validation")
        print("2. Ice Cream Shop")
        print("3. Magic Cafeteria")
        print("4. Cinema Ticket System")
        print("5. Exit")

        op = int(input("Select an option: "))

        if op == 1:
            rg()

        elif op == 2:
            ri()

        elif op == 3:
            rc()
        
        elif op == 4:
            rct()
        elif op == 5:
            print("Closing program...")
            start = 0

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()