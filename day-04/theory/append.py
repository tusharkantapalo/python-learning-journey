num = int(input("Enter the number: "))
d = []
for i in range(1, num + 1):
    if (i % 3 == 0) and (i % 5 == 0):
        d.append("FizzBuzz")
    elif (i % 3 == 0):
        d.append("Fizz")
    elif (i % 5 == 0):
        d.append("Buzz")
    else:
        d.append(i)
print(d)