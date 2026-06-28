n = int(input("Enter the number of inputs: "))
d = {}
for i in range(n):
    d[i] = input("Enter: ")
print(d)
del(d[1])
print(d)
d.clear() #to delete all the values
print(d)