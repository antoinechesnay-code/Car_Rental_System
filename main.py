from car_rental_system import *
from util import *
import sys
import time

def secret_admin_menu(lboroStock):
    pass
    print()
    print("Functionality not implemented yet!")
    print()
    # to write
    # The Rental Shop(s) can:
    # Issue a bill when the customer returns their car,
    # Display available inventory and prices when a customer enquires,
    # Process rent requests from customers after verifying stock availability.




# import car_rental_system
def rent_a_car(lboroStock):
    # Get customer name first
    customer_name = get_not_empty_string("Enter your name: ")  
    #Check whether customer is a VIP
    is_vip = get_yes_no_answer("Are you a VIP customer (yes/no): ")
    # Then ask for the car
    car_to_rent = input("Please enter the name of the car you want to borrow: ")

    # Get the number of days for the location
    rental_days = get_positive_integer("How many days would you like to rent this car for? ")
    # Now book the renting of the car in the system
    if is_vip == True:
        customer = VIP(customer_name)
    else:
        customer = Customer(customer_name)
    lboroStock.rentcar(customer, customer, car_to_rent, rental_days)  


def return_a_car(lboroStock):
    customer_name = input("what is your name: ")
    car_to_return = input("What car are you returning: ")
    lboroStock.returncar(customer_name, car_to_return)

    # customer.returncar(input("What car are you returning?"))
    # LboroStock.returncar(input("Enter your name: "))  
    
    # create bill for customer 
# elif user_input == 4: # Leave a review
#     LboroStock.feedback()
    # customer_review = input("Please rate out customer services from 1(extremely bad) to 5(extremely good)")

def customers_menu(lboroStock):
# try:
    print(f"{CBOLD}{CVIOLETBG2}Welcome to Loughborough car rental shop. {CGREENBG} For secret admin menu, type 999{CEND}")
    print(f"{CBOLD}1{CEND} View current inventory. ")
    print(f"{CBOLD}2{CEND} Rent a car. ")
    print(f"{CBOLD}3{CEND} Return a car.")
    print(f"{CBOLD}4{CEND} Exit")
    user_input_string = input(CVIOLET+"Please choose 1, 2, 3 or 4 to proceed: "+CBLACK)
    user_input = int(user_input_string)
    if user_input == 1: # View inventory
        lboroStock.showInventory() 
    elif user_input == 2: # Rent car
        rent_a_car(lboroStock)
        
    elif user_input == 3: # Return a car
        return_a_car(lboroStock)

    elif user_input == 4: # Exit
        print("Thank you for using our services! See you again.")
        time.sleep(2)
        animation()
        # Rather than completely exiting
        #exit()

    elif user_input == 999: # Return a car 
        secret_admin_menu(lboroStock)

    else:
        print(f"{CRED}{CBLINK2}\n{user_input_string} is not a valid menu selection. \n"+CEND+CBLACK)

    # except Exception as e:
    #     print(f"{CRED}{CBLINK2}\n{user_input_string} is not a valid menu selection. \n"+CEND+CBLACK)

if __name__ == "__main__":

    lboroStock = RentalShop({
        'Hatchback': 10, 
        'Sedan': 10, 
        'SUV': 10})
    
    # lboroStock.showInventory()
    # customer = Customer()
    # rented = {}



    animation()
    while True:
    # This section welcome prospective customers or returners and gives them options on how to proceed

        customers_menu(lboroStock)