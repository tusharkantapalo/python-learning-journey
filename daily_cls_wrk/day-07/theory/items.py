n = int(input("Enter the number of inputs: "))
d = {}
for i in range(n):
    d[i] = input("Enter: ")
print(d.items())
'''In the output each item is a tuple'''