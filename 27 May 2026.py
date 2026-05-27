#TYPE CASTING
age=input("Enter your age: ")
print(type(age)) #Here it is a string
age=int(input("Enter your age: "))
print(type(age)) #Here it is an integer
#OPERATORS
x=input("Enter first number: ")
y=input("Enter second number: ")
print(x+y) #we will get the output as 2020, as these are strings
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
print(x+y) #we will get the value as 40
import math
print(math.floor(3.5))
print(math.ceil(3.5))
print(round((7/3), 3))