def flatten(lst):
    result = []
    for item in lst:
        if type(item) == list:
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
nested = [1, [2, 3], [4, [5, 6]], 7]
print("Flattened:", flatten(nested))