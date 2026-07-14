n = int(input("Enter the number of inputs: "))
d = []
for i in range(n):
    d.append(int(input("Enter: ")))
sum = 0
for i in d:
    sum += i
avg = sum / len(d)
d1 = []
for i in range(len(d)):
    if d[i] >= avg:
        d1.append(d[i])
print(d1)