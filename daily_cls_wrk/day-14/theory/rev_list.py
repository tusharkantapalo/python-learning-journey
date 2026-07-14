n = int(input("Enter the number of inpputs: "))

list = []

for i in range(n):
    list.append(int(input("Enter: ")))

list_rev_sorted = sorted(list, reverse = True)
list_sorted = sorted(list) #by default ascending

print(f"Reversed sorted list: {list_rev_sorted}")
print(f"Sorted list: {list_sorted}")
