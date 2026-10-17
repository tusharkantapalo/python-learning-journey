def findGreat(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        grt = num1
    elif num2 > num1 and num2 > num3:
        grt = num2
    else:
        grt = num3

    return grt

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

res = findGreat(n1, n2, n3)

print(f"Largest number is {res}.")
