a, b, c = int(input("Enter a: ")), int(input("Enter b: ")), int(input("Enter c: "))
'''if a > b:
    if a > c:
        lerge = a
    else:
        large = c
elif b > c:
    large = b
else:
    large = c
print(f"Largest number is: {large}")'''
large = a if a > b and a > c else (b if b > c else c)
print(f"Largest number is: {large}")