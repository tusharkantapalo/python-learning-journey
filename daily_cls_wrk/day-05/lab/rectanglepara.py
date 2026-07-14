import math
len = int(input("Enter the length: "))
width = int(input("Enter the width: "))
peri = 2 * (len + width)
area = len * width
dia = math.sqrt((len * len) + (width * width))
print(f"Perimeter is {peri}")
print(f"Area is {area}")
print(f"Diagonal is {dia}")