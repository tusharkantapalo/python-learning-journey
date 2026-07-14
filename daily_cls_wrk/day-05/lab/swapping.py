a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"Numbers before swapping is: {a}, {b}")
temp = a
a = b
b = temp
print(f"Numbers after swapping is: {a}, {b}")