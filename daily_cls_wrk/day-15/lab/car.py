'''
1. Blueprint Structure (Class & Attributes)
• Class Attribute: showroom_name = "Mega Motors" (This stays identical for all car objects).
• Constructor (_init_): Must accept three parameters for each car: brand, engine_type (e.g., Petrol, Diesel, EV), and base_price.
2. Actions (Methods)
• Method 1 (show_car_card): This method should return a string containing the car details.
• Format: "This is a [brand] car running on [engine_type] available at [showroom_name]."
• Method 2 (calculate_on_road_price): This method must accept a tax amount, add it to base_price to calculate final price,
and print it to the screen.
• Formula: final_price = base_price + tax
3. Execution (Object Creation & Testing)
• Create an object named my_car with the following data: "Tata", "EV", 1500000.
• Call and print the result of show_car_card().
• Call calculate_on_road_price(50000) to display final calculated price.
'''


class MegaMotors:

    def __init__(self, brand, engine_type, base_price):
        self.car_brand = brand
        self.car_engine_type = engine_type
        self.car_base_price = base_price

    def car_card(self):
        return f"This is a {self.car_brand} car running on {self.car_engine_type} available at Mega Motors"
    
    def cal_onroad_price(self, tax):

        onroad_price = self.car_base_price + tax

        print(f"Onroad price of this car is {onroad_price}/- rupees")
        
car_brand = input("Enter the brand of the car: ")
engine_type = input("Enter the engine type of the car: ")
base_price = int(input("Enter the base price of the car: "))
tax = int(input("Enter the tax amount in rupees: "))

my_car = MegaMotors(car_brand, engine_type, base_price)

res = my_car.car_card()

print(res)

my_car.cal_onroad_price(tax)
