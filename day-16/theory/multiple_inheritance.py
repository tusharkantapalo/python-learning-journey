class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
class Surface(Animal):
    def __init__(self, name, food):
        Animal.__init__(self, name)
        self.food = food

    def get_food_name(self):
        return self.food
    
class Water(Animal):
    def __init__(self, name, food):
        Animal.__init__(self, name)
        self.food = food

    def get_food_name(self):
        return self.food
    
class Turtle(Surface, Water):
    def __init__(self, name, food):
        super().__init__(name, food)

obj = Turtle("turtle", "grass")

res = obj.get_food_name()

print(res)
