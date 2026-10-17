def calc(n):

    if n == 0:
        return 0

    return n + calc(n - 1)

n = int(input("Enter the number: "))

res = calc(n)

print(f"The sum is {res}.")
