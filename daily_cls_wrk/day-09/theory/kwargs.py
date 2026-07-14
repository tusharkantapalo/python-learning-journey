def func(**kwargs):
    print(kwargs)
n = int(input())
d = {}
for i in range(n):
    key = input("Key: ")
    value = input("Value: ")
    d[key] = value
func(**d)