n1 = int(input("Enter the size of first list: "))
n2 = int(input("Enter the size of second list: "))
d1 = []
d2 = []
for i in range(n1):
    d1.append(int(input("Enter in list-1: ")))
for i in range(n2):
    d2.append(int(input("Enter in list-2: ")))
d3 = [*d1, *d2]
print(d3)