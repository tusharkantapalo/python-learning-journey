n = int(input("Enter the number of inputs: "))

l = []
for i in range(n):
    l.append(int(input("Enter: ")))

target = int(input("Enter the target: "))

l1 = []

'''for i in l:
    for j in l:
        if i + j == target:
            l1.append((i, j))'''

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] + l[j] == target:
            l1.append((l[i], l[j]))
else:
    print("Not found")

print(f"The pairs are: {l1}")
