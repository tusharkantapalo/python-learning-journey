'''Write aprogram to arrange the list of tuple by its first element'''

n = int(input("Enter the number of inputs: "))

list = []

for i in range(n):
    list.append((int(input("Enter 1st element: ")), int(input("Enter 2nd element: "))))

list_sorted = sorted(list, key = lambda x: x[0], reverse = True)

print(f"Sorted list is: {list_sorted}")
