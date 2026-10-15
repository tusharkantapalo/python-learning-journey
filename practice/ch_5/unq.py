n = int(input("Enter the number of elements: "))

s = set()

for i in range(0, n):

    num = int(input("Enter the element: "))

    s.add(num)

print(f"The unique numbers are: {s}")
