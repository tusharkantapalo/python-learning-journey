n1 = int(input("Enter the size of first dictionary: "))
n2 = int(input("Enter the size of second dictionary: "))
d1 = {}
d2 = {}
for i in range(n1):
    key = int(input("Key: "))
    value = input("Value: ")
    d1[key] = value
for i in range(n2):
    key = int(input("Key: "))
    value = input("Value: ")
    d2[key] = value
d3 = {**d1, **d2}
d1.update(d2)
print(d3)
print(d1)