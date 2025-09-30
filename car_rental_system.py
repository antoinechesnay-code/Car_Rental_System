
'''
Car Rental System Implementation

This module provides classes for managing a car rental business:
- RentalShop: Manages car inventory and rental operations
- Customer: Represents basic customer functionality
- VIP: Represents a VIP customer with special pricing
'''

# import pytest
# from typing import Dict

 

from util import *

class RentalShop():
    def __init__(self, carsowned):
        self.cars = carsowned
        # using a customer object as a key to the rented dictionary
        # https://realpython.com/lessons/restrictions-dictionary-keys-and-values/
        # self.rented is a nested dictionary: key is client, and nested key is car() and nested value is days
        self.rented = {} #initialise rented dicitonary 
        # for cars in carsowned:
        #     self.rented[cars] = {} 
        # self.ratings = [] #initialise feedback list


    def showInventory(self):
        if not self.cars:
            print(f"{CRED}Sorry, we have no cars available at the moment.{CBLACK}")
        else:
            print(f"{CBOLD}{CVIOLETBG2}Cars available for rent:{CEND}")
            for car, count in self.cars.items():
                if count>0:
                    print(f"{CGREEN}- {car}: {count} available{CBLACK}")
                else:
                   print(f"{CRED}- {car}: unavailable{CBLACK}") 
        print()



    def rentcar(self,customer, name, carname, days):

    # found_customer_name = False
    # for car_type, info_customer in self.rented.items():
    #     if info_customer["name"] == name
    #         found_customer_name = True
    #         break
    # if not found_customer_name:

        if customer.name in self.rented: # and any(self.rented[customer.name])
                print("You have already rented a car. Return your car first before renting another one. ")
        elif carname not in self.cars:
            print(f"Sorry, {carname} is not a valid car name.")
        elif self.cars[carname] > 0:
            self.cars[carname] -= 1
            #At the top i initialise the dictionary - 
            # if customer.name not in self.rented:
            if customer.name not in self.rented:
                self.rented[customer.name] = {}
            self.rented[customer.name][carname] = days #self.rented[customer.name]    ({carname:days}) # adds carname and days within the value (carname is nested key and days is nested value)
            price = self.getprice(carname, days, name.is_vip) #Pass the is_vip flag
            # If available, display the following
            #message (or something similar) to the customer: “You have rented a
            #{ } car for { } days. You will be charged { } per day, We hope that you
            #enjoy our service." Update the stock accordingly.
            # If unavailable, inform the customer that the car is out of stock.
            print(f"Thank you {name}, your {carname} has been issued. You will incur a fee of £{price}. Please return this on the scheduled date. ")
        elif carname in self.cars and self.cars[carname] == 0:
            print(f"Sorry, {carname} is not available for rent currently, please try again later.")
        else:
            print(f"Sorry, {carname} is not a valid car name.")

# VIP daily rate: Hatchback £20, sedan £35, SUV £80 per day.
# Less than a week (< 7 days): Hatchback £30, sedan £50, SUV £100 per day.
# A week or longer (≥ 7 days): Hatchback £25, sedan £40, SUV for £90 per day.

    def getprice(self, carname, days, is_vip): #Corrected definition
        prices = { #Corrected prices dictionary
            'Hatchback': 20 if is_vip else (25 if days >= 7 else 30),
            'Sedan': 35 if is_vip else (40 if days >= 7 else 50),
            'SUV': 80 if is_vip else (90 if days >= 7 else 100)
        }
        if carname in prices:
            return prices[carname] * days
        else:
            return "Invalid car name. "

    

    # def returncar(self, name, carname):
    #     if name in self.rented and carname in self.rented[name]:
    #         self.rented[name].remove(carname)  # Remove car from renter
    #         self.cars[carname] += 1  # Increase available cars
    #         print(f"Thank you {name}, your return of {carname} is processed.")
    #         print(f"Your fee for today is £{self.getprice(name, carname, days_rented, False)}")
    #         if not self.rented[name]:  # Remove renter if they have no more cars
    #             del self.rented[name]
    #     else:
    #         print("Invalid return information. Please check your details.")

    def returncar(self, name, carname):
        if name in self.rented and carname in self.rented[name]:
            days_rented = self.rented[name][carname] #Retrieve days rented
            del self.rented[name][carname]  # Remove car from renter's dict
            self.cars[carname] += 1
            price = self.getprice(carname, days_rented, False) # Calculate price, assuming not VIP on return.
            print(f"Thank you {name}, your return of {carname} is processed.")
            print(f"Your fee for the rental is £{price}") # Print calculated price
            if not self.rented[name]:  # Remove renter if they have no more cars
                del self.rented[name]
        else:
            print("Invalid return information. Please check your details.")

    # def feedback(self):
    #     try:
    #         rating = int(input("Please rate out customer services from 1(extremely bad) to 5(extremely good)"))
    #         if 1 <= rating <= 5:
    #             self.ratings.append(rating)
    #             print("Thank you for your feedback!")
    #             items = len(self.ratings)
    #             if items > 0:
    #                 avg_rating = (sum(self.ratings)/items)
    #                 print("Average rating: ", avg_rating)
    #             print("Number of reviews: ", items)
    #         else:
    #             print("Invalid rating. Please enter a number between 1 and 5.")
    #     except ValueError:
    #         print("Invalid input. Please enter a valid number.")



class Customer():

    # Initialise a new instance with the name of the customer
    def __init__(self, name: str):
        self.name = name


    # print the customer name
    def __str__(self) -> str:
        return f"Name: {self.name})" #may want to also print the car currently rented if any

    def requestcar(self):
        self.car = input("Please enter the name of the car you want to borrow: ")
        return self.car

    def is_vip(self) -> bool:
        return False

class VIP(Customer):
    # Initialise a new instance with the name of the customer
    def __init__(self, name: str):
        self.name = name

    def is_vip(self) -> bool:
        return True


if __name__ == "__main__":
    pass
    # include test using Pytest
    #
    # Please see
    # https://realpython.com/pytest-python-testing/

    # These tests will be run when executing car_rental_system.py

