n = int(input("Enter the number of inputs: "))

l = []
for i in range(n):
    l.append(int(input("Enter: ")))

print(f"Before sorting: {l}")

l1 = sorted(l)
print(f"After sorting: {l1}")

l.sort() #inplace
print(f"After sorting: {l}")