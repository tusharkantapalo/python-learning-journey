n = int(input("Enter the number: "))

for i in range(1, n + 1):
    for j in range(n - i):

        print(" ", end="")

    for g in range(i):

        print("*", end="")

    for h in range(i - 1):

        print("*", end="")

    print("\n")
