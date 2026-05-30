n = int(input("Enter the number of inputs: "))
d = []
for i in range(n):
    d.append(int(input("Enter: ")))
max = 0
for i in d:
    if max < i:
        max = i
d1 = [] * max
j = 0
for i in range(1, max):
    if d[j] == i:
        j += 1
        continue
    else:
        d1.append(i)
print(d1)