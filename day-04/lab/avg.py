n = int(input("Enter how many numbers: "))
sum = 0
for i in range(1, n + 1):
    num = int(input("Enter a number: "))
    sum += num
avg = sum / n
print(f"Average is: {avg}")