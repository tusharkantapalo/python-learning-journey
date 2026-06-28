n = int(input("Enter the number of inputs: "))
char = input("Enter the character: ")
d = []
for i in range(n):
    d.append(input("Enter: "))
print(d.index(char, 0, len(d)))