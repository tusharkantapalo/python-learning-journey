'''num = int(input("Enter the number: "))
for i in range(num, 0, -1):
    print(i)'''


def print_desc(num):

    if num == 0:
        return

    print(num)
    print_desc(num - 1)


num = int(input("Enter the number: "))
print_desc(num)