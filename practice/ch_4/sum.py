n = int(input("Enter the number of elements: "))

lst = []

print ("Enter the elements of the list: ")
for i in range(0, n):
    num = int(input("Enter the number: "))
    lst.append(num)

sum = 0

for i in range(0, n):
    sum = sum + lst[i]

print (f"Sum is {sum}.")
