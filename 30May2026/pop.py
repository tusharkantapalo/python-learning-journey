n = int(input("Enter number of digits: "))
d = []
for i in range(n):
    d.append(int(input("Enter: ")))
print(d)
print(d.pop(0))
print(d.pop(2))
print(d.pop()) #by default last index