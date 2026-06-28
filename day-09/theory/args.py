def dd_number(*args):
    print(args)
    print(sum(args))
n = int(input())
d = ()
for i in range(n):
    d += (i,)
dd_number(*d)