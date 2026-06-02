def check(num): #function name should be a verb
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
num = int(input("Enter the number: "))
check(num)