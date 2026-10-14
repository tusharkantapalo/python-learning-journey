n = int(input("Enter the number of inputs: "))

tpl = ()

for i in range(0, n):
    num = int(input("Enter the number: "))
    tpl = tpl + (num,)

print(tpl)
tpl1 = float(tpl)

print(tpl1)                                     #error is showing
