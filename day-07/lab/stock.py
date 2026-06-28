n = int(input("Enter the number of products: "))
d = {}
for i in range(n):
    prdct = input("Enter the name of the product: ")
    qnt = int(input("Enter the quantity: "))
    d[prdct] = qnt
lowest = min(d.values())
for prdct in d:
    if d[prdct] == lowest:
        prdct1 = prdct
print(f"{prdct1} is in lowest stock and its quantity is {d[prdct1]}")