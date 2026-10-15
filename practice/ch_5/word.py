n = int(input("Enter the number of inputs: "))

dict = {}

for i in range(0, n):
    key = input("Enter the key: ")
    val = input("Enter the value: ")

    dict[key] = val

print(f"The dictionary is: {dict}")
