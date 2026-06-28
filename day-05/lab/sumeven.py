num = int(input("Enter the nuber: "))
sum = 0
for i in range(num + 1):
    if i % 2 == 0:
        sum += i
print(f"Sum is {sum}")