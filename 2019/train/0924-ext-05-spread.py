def spread(origin, result=[]):
    for i in origin:
        if type(i) is list:
            spread(i, result)
        else:
            result.append(i)
    return result

def spread_2(array:list):
    result = []
    while array:
        for i, v in enumerate(array):
            if isinstance(v, list):
                array = v + array[1:]
                break
            else:
                result.append(v)
                array.pop(i)
                break
    return result

print(spread([1, [2, 3, [4, [5, [6]]], [7], 8, 9]]))  # [1,2,3,4,5,6,7,8,9]
