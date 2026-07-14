def is_even(num):
    if num % 2:
        return False
    return True
res = list(filter(is_even, [1, 2, 3, 4, 5, 6]))
print(res)