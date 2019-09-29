import math


def binary_search(origin: list, target: int):
    l_index = 0
    r_index = len(origin) - 1
    while l_index <= r_index:
        cursor = (l_index + r_index) // 2
        if origin[cursor] == target:
            return cursor
        else:
            if target < origin[cursor]:
                r_index = cursor - 1
            else:
                l_index = cursor + 1
    return None


def get_reverse(origin: str):
    return origin[::-1]


def get_mid_number(origin: list):
    length = len(origin)
    if length == 0:
        return None
    return round((origin[length // 2] + origin[length // 2 - 1]) / 2, 1) if length % 2 == 0 else origin[length // 2]

print(get_mid_number([2,3,4]))