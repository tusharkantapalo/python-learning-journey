'''
-> Abstract class should not have any implementation
-> Abstract class should not have __init__ method
-> If I inherit any abstract class, then I have to implement
    all the methods
'''


from abc import ABC
from abc import abstractclassmethod

class Shape(ABC):

    def __init__(self, name):
        self.name = name

    @abstractclassmethod
    def area(self):
        pass
    @abstractclassmethod
    def perimeter(self):
        pass

#shape = Shape("Cube") #This can not be done

class Square(Shape):

    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side
    

obj = Square("Square", int(12))

res1 = obj.area()

print(res1)

res2 = obj.perimeter()

print(res2)
