from gym_acces import run_gym_acces as rg
from ice_cream_shop import run_ice_cream_shop as ri
from magic_cafeteria import run_cafeteria as rc
from cinema_ticket_system import run_cinema_ticket as rct
from pet_shop_recommendation import run_pet_shop as rps
from parking_lot_system import run_parking_lot as rpl
from hair_salon import run_hair_salon as rhs
from sport_shop import run_sport_store as rss
from spa_service_system import run_spa_services as rs
from dance_academy import run_dance_academy as rdc
from supa_ice_cream import run_ice_cream_clients as ric
from gym_performance import run_gym_performance as rgp
from cafeteria_sales_system import run_cafeteria_discount as rcd
from cinema_room_control import run_cinema_control as rcc

def main():

    start = 1

    while start != 0 :

        print("\nMAIN MENU")
        print("-"*40)
        print("1. Ice Cream Shop")
        print("2. Gym Age Validation")
        print("3. Magic Cafeteria")
        print("4. Cinema Ticket System")
        print("5. Pet Shop Recommendation")
        print("6. Parking Lot System")
        print("7. Hair Salon Schedule")
        print("8. Sport Shop Price Counter")
        print("9. Spa Service System")
        print("10. Dance Academy Attendance")
        print("11. Supa Ice Cream")
        print("12. Gym Weekly Performance")
        print("13. Cafeteria Sales Discount")
        print("14. Cinema Royal Control")
        print("21. Exit")

        op = int(input("Select an option: "))

        if op == 1:
            ri() 

        elif op == 2:
            rg()

        elif op == 3:
            rc()
        
        elif op == 4:
            rct()

        elif op == 5:
            rps()

        elif op == 6:
            rpl()

        elif op == 7:
            rhs()

        elif op == 8:
            rss()

        elif op == 9:
            rs()

        elif op == 10:
            rdc()

        elif op == 11:
            ric()

        elif op == 12:
            rgp() 

        elif op == 13:
            rcd()  
        
        elif op == 14:
            rcc()  

        elif op == 21:
            print("Closing program...")
            start = 0

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()