a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
try:
    res = a / b
except ZeroDivisionError:
    print("Zero Division Error!")
except ValueError:
    print("Name Error!")
else:
    print(f"Result is calculated successfully: {res}")
finally:
    print("Execution sequence completely finalised.")