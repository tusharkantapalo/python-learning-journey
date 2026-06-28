import math
len = int(input("Enter the length: "))
peri = 4 * len
area = len * len
dia = math.sqrt((len * len) + (len * len))
print(f"Perimeter is {peri}")
print(f"Area is {area}")
print(f"Diagonal is {dia}")