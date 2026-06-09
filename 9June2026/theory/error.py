def divide_two_nos_zeroDivisionError(a: int, b: int) -> float:
    try:
        return(a / b)
    except ZeroDivisionError: #it will except the error if happened
        return "Zero Division Error!" #it will only deal with Zerodivision error


def divide_two_nos_NameError(a: int, b: int) -> float:
    try:
        return a / c
    except NameError:
        return "Name Error!" #it will only deal with Name error


a = int(input("Enter the value of a: "))
b = int(input("Enter the value of a: "))
'''if b == 0:
    print("Division not possible.")
else:
    print(a / b)'''
res1 = divide_two_nos_zeroDivisionError(a, b)
print(res1)

res2 = divide_two_nos_NameError(a, b)
print(res2)
