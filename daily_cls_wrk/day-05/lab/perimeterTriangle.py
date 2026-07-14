print(f"Enter 3 length: ")
d = [0] * 3
peri = 0
for i in range(3):
    d[i - 1] = int(input("Enter: "))
for i in d:
    peri += i
print(f"Perimeter is {peri}")