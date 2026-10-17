def calc(C):
    f = ((c * 9) / 5) + 32

    return f

c = int(input("Enter the temperature: "))

res = calc(c)

print(f"{c} degree C = {res} degree F")
