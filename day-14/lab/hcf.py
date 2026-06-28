try:
    def hcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("HCF = ", hcf(num1, num2))
except Exception:
    print("Something wrong happened!")

finally:
    print("__________CODE EXECUTION COMPLETED__________")