"""
## 4. Shape Hierarchy with an Abstract Method  *(Medium)*

=================================================
SHAPE HIERARCHY (PARENT + 3 CHILDREN)
=================================================

Problem Statement:
Build a small inheritance hierarchy:

   Shape   (parent / "abstract" base)
   ├── Circle
   ├── Rectangle
   └── Triangle    (uses Heron's formula for
                    area)

The parent class declares the shape's name
and the methods area() and perimeter() — but
these methods just RAISE NotImplementedError
so that any child class is FORCED to override
them.

This problem teaches:
   - one parent, multiple children
   - the "abstract method" pattern using
     NotImplementedError
   - using super().__init__() in each child
   - storing different attributes per child

-------------------------------------------------
Instructions:
1. Parent class:
      class Shape:
          def __init__(self, name):
              self.name = name

          def area(self):
              raise NotImplementedError(
                  "Child classes must override area()"
              )

          def perimeter(self):
              raise NotImplementedError(
                  "Child classes must override perimeter()"
              )

          def describe(self):
              print(f"{self.name}: "
                    f"area={self.area()}, "
                    f"perimeter={self.perimeter()}")

2. Child class Circle:
      __init__(self, radius)
          - super().__init__("Circle")
          - self.radius = radius
      area()       -> 3.14159 * r * r
      perimeter()  -> 2 * 3.14159 * r

3. Child class Rectangle:
      __init__(self, length, width)
          - super().__init__("Rectangle")
          - store length, width
      area()       -> length * width
      perimeter()  -> 2 * (length + width)

4. Child class Triangle:
      __init__(self, a, b, c)
          - super().__init__("Triangle")
          - store sides a, b, c
      perimeter()  -> a + b + c
      area()       -> Heron's formula:
                       s = perimeter / 2
                       area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

5. In the driver code:
      - create one Shape and call describe()
        in a try/except to see the
        NotImplementedError
      - create at least one Circle, one
        Rectangle, one Triangle
      - put them in a LIST and use a for loop
        to call describe() on each shape
6. Do NOT use:
   - the math module (use 3.14159 as PI)
   - any external library

-------------------------------------------------
Input Example:
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5),
]

Output Example:
Circle: area=78.53975, perimeter=31.4159
Rectangle: area=24, perimeter=20
Triangle: area=6.0, perimeter=12
Shape itself raises NotImplementedError when describe() is called.

-------------------------------------------------
Explanation:
- The parent Shape provides the SHARED logic
  (name + describe()) but refuses to compute
  area/perimeter on its own.
- Each child OVERRIDES area() and perimeter()
  with formulas appropriate for that shape.
- describe() works on ALL shapes through
  POLYMORPHISM: the same method call produces
  different results depending on the actual
  object type.
=================================================

"""


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError(
            "Child classes must override area()"
            )

    def perimeter(self):
        raise NotImplementedError(
            "Child classes must override perimeter()"
            )

    def describe(self):
        print(f"{self.name}: "
            f"area={self.area()}, "
            f"perimeter={self.perimeter()}")
        
class Circle(Shape):

    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
class Ractangle(Shape):

    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
class Triangle(Shape):

    def __init__(self, a, b, c):
        super().__init__("Triangle")
        self.a = a
        self.b = b
        self.c = c
        self.s = (a + b + c) / 2

    def area(self):
        return (self.s * (self.s - self.a) * (self.s - self.b) * (self.s - self.c)) ** 0.5
    
    def perimeter(self):
        return self.a + self.b + self.c
    

try:
    shape = Shape("Shape")
    shape.describe()
except NotImplementedError as e:
    print(e)

shapes = []

n = int(input("Enter number of shapes: "))

for i in range(n):

    shape_type = input(
        "Enter shape type (circle/rectangle/triangle): "
    ).lower()

    if shape_type == "circle":
        radius = float(input("Enter radius: "))
        shapes.append(Circle(radius))

    elif shape_type == "rectangle":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        shapes.append(Ractangle(length, width))

    elif shape_type == "triangle":
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        c = float(input("Enter side c: "))
        shapes.append(Triangle(a, b, c))

    else:
        print("Invalid shape type!")

for shape in shapes:
    shape.describe()

print("\nShape Details:\n")

for shape in shapes:
    shape.describe()
