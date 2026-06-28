n = int(input("Enter the number of inputs: "))
d = []
for i in range(n):
    d.append(input("Enter: "))
for i in range(len(d) - 1, -1, -1):
    if len(d[i]) <= 5:
        d.pop(i)
print(d)