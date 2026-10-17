num = int(input("Enter the number: "))

cnt = 0

for i in range(1, num + 1):
    if (num % i == 0):
        cnt += 1

if (cnt == 2):
    print(f"{num} is prime.")
else:
    print(f"{num} is not prime.")
