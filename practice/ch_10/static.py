import math


class Calculator:

    @staticmethod
    def greet():
        print("\nHello!")

    def __init__(self, n):
        self.num = n

    def sq(self):
        return self.num * self.num

    def sqrt(self):
        return math.sqrt(self.num)

    def cub(self):
        return self.num * self.num * self.num


num = int(input("Enter the number: "))

ob1 = Calculator(num)

ob1.greet()
res1 = ob1.sq()
res2 = ob1.cub()
res3 = ob1.sqrt()

print(f"Square of {num} = {res1}\nCube of {num} = {res2}\nSquare root of {num} = {res3}")
