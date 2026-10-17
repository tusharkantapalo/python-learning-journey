n = int(input("Enter the number of persons: "))

l = []

for i in range(0, n):
    name = input("Enter the name: ")
    l.append(name)

for nam in l:
    print(f"Good Morning {nam}!")
