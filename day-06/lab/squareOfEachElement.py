n = int(input("Enter the number of inputs: "))
d = []
for i in range(n):
    d.append(int(input("Enter: ")))
for i in range(len(d)):
    d[i] = d[i] * d[i]
print(d)