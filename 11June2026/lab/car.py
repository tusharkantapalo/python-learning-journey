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
