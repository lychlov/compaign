import math


def get_ugly_number(index):
    if index == 1:
        return 1
    ugly_numbers = [1]
    m2 = m3 = m5 = 0
    while len(ugly_numbers) < index:
        current = min(ugly_numbers[m2] * 2, ugly_numbers[m3] * 3, ugly_numbers[m5] * 5)
        ugly_numbers.append(current)
        if current == ugly_numbers[m2] * 2:
            m2 += 1
        if current == ugly_numbers[m3] * 3:
            m3 += 1
        if current == ugly_numbers[m5] * 5:
            m5 += 1

    return ugly_numbers[-1]


print(get_ugly_number(150))
