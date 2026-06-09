def divide_two_nos(a: int, b: int) -> float:
    try:
        return(a / b)
    except: #it will except the error if happened
        pass


a = int(input("Enter the value of a: "))
b = int(input("Enter the value of a: "))
'''if b == 0:
    print("Division not possible.")
else:
    print(a / b)'''
res = divide_two_nos(a, b)
print(res)
