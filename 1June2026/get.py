n = int(input("Enter the number of inputs: "))
d = {}
for i in range(n):
    d[i] = input("Enter: ")
print(d)
print(d.get(1))
print(d.get(5))
res = d.get(6)
print(type(res))