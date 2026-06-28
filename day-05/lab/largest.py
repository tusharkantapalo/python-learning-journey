'''n = int(input("Enter the number of digits: "))
d = [0] * n
for i in range(n):
    d[i - 1] = int(input("Enter the number: "))
max = 0
for i in d:
    if i > max:
        max = i
print(f"Largest is {max}.")'''
#using append
n = int(input("Enter the number of digits: "))
d = []
for i in range(n):
    d.append(int(input("Enter: ")))
max = 0
for i in d:
    if i > max:
        max = i
print(f"Maximum number is: {max}")