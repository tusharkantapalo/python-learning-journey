n = int(input("Enter the number: "))
d = [0] * n
for i in range(1, n + 1):
    if (i % 3 == 0) and (i % 5 == 0):
        d[i - 1] = "FizzBuzz"
    elif (i % 3 == 0):
        d[i - 1] = "Fizz"
    elif (i % 5 == 0):
        d[i - 1] = "Buzz"
    else:
        d[i - 1] = str(i)
print(d)