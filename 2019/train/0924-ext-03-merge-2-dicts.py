def merge_two_dicts(a, b):
    a.update(b)
    return a


a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}
print(merge_two_dicts(a, b))
# {'y': 3, 'x': 1, 'z': 4}
