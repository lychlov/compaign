def get(d, key, value=None):
    return d.get(key, value)

def get_2(d,key,value=None):
    try:
        return d[key]
    except:
        return value if value else None


d = {'a': 1, 'b': 2}

print(get_2(d, 'c',2))
