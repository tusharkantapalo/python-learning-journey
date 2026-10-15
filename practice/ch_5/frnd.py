n = int(input("Enter the number of friends: "))

dict = {}

for i in range(0, n):
    name = input("Enter your name: ")
    lang = input("Enter your language: ")

    dict[name] = lang

print(f"The details are: {dict}")
