n = int(input("Enter the number of names: "))

lst = []

for i in range(0, n):
    name = input("Enter the name: ")
    lst.append(name)

fnd = input("Enter the name to find: ")

if fnd in lst:
    print(f"{fnd} is found in this list.")
else:
    print(f"{fnd} is not found in this list.")
