'''
Step 1: Create the Blueprint (Abstraction)
Create an abstract base class named RentalVehicle.
• Properties: Every vehicle must have a constructor (_init__) that accepts and sets a brand and a model.
• Abstract Method 1:
calculate_rent(self, days: int)
→ float (No logic inside, just a blueprint).
• Abstract Method 2:
get_fuel_type(self) -> str (No logic inside, just a blueprint)

Step 2: Create the Subclasses (Polymorphism) [1]
Create two normal classes that inherit from RentalVehicle. 
They must implement the abstract methods with their own specific rules: [1]
Car Class
• calculate_rent: Multiply the number of days by a flat rate of $50.
• get_fuel_type: Always return the text string
"Gasoline".
1. ElectricScooter Class
• calculate_rent:
Calculate a flat base activation fee of $15, plus $5 for every day rented.
• get_fuel_type: Always return the text string
"Electric Battery"

Step 3: Create the Standalone
Execution Function
Write a separate, independent function named
print_receipt(vehicle:
RentalVehicle, days: int).
• This function must not check if the vehicle is a car or a scooter 
  (do not use if/else statements or isinstance)).
• It should accept any vehicle object, automatically call calculate_rent(days) and 
  get_fuel_type(), and print a formatted receipt displaying the brand, model, 
  fuel type, and final cost.
'''
from abc import ABC, abstractmethod

class RentalVehicle(ABC):

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def calculate_rent(self, days: int) -> float:
        pass

    @abstractmethod
    def get_fuel_type(self) -> str:
        pass

class Car(RentalVehicle):

    def __init__(self, brand, model):
        super().__init__(brand, model)

    def calculate_rent(self, days: int) -> float:
        return days * 50

    def get_fuel_type(self) -> str:
        return "Gasoline"

class ElectricScooter(RentalVehicle):

    def __init__(self, brand, model):
        super().__init__(brand, model)

    def calculate_rent(self, days: int) -> float:
        return 15 + (days * 5)

    def get_fuel_type(self) -> str:
        return "Electric Battery"

def print_receipt(vehicle: RentalVehicle, days: int):
    cost = vehicle.calculate_rent(days)
    fuel = vehicle.get_fuel_type()

    print("\n----- RENTAL RECEIPT -----")
    print(f"Brand: {vehicle.brand}")
    print(f"Model: {vehicle.model}")
    print(f"Fuel Type: {fuel}")
    print(f"Days Rented: {days}")
    print(f"Final Cost : ${cost:.2f}")


car_brand = input("Enter car brand: ")
car_model = input("Enter car model: ")

scooter_brand = input("Enter scooter brand: ")
scooter_model = input("Enter scooter model: ")

car = Car(car_brand, car_model)
scooter = ElectricScooter(scooter_brand, scooter_model)

days = int(input("Enter number of rental days: "))

print_receipt(car, days)
print()
print_receipt(scooter, days)
