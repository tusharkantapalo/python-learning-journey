n = int(input("Enter the number of inputs: "))

list = []
large = 0

for i in range(0, n):
    n = int(input("Enter the number: "))
    list.append(n)

for i in list:
    if (i > large):
        large = i

print(f"The largest number is {large}")
