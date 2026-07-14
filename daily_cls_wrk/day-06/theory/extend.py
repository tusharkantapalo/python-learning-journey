exp = input("Enter comma separated numbers: ")
d = []
print(exp)
d = exp.split(sep = ',')
print(d)
d.append('123')
print(d)
d.extend(['1', '2', '3'])
print(d)