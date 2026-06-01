n = int(input("Enter the number of inputs: "))
d = {}
for i in range(n):
    d[i] = input("Enter: ")
print(d)
print(d[2])
print(type(d))
#list can be a value but keys always should be an immutable object