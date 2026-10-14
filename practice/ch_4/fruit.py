num = int(input("Enter the number of fruits: "))

lst = []

for i in range(1, num + 1):
    frt = input("Enter: ")
    lst.append(frt)

for i in range(0, num):
    print(f"{lst[i]}")
