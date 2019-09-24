def difference(a: list, b: list):
    return list(set(a) - set(b))


print(difference([1, 2, 3], [1, 2, 4]))
