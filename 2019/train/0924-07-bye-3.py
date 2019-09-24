def bye_3(n):
    circle = list(range(1, n + 1))
    bye = 0
    bye_count = 0
    while bye_count < len(circle) - 1:
        for i in range(len(circle)):
            if circle[i] != 0:
                if bye == 3:
                    bye = 1
                else:
                    bye += 1
                if bye == 3:
                    circle[i] = 0
                    bye_count += 1
    for i in circle:
        if i != 0:
            return i


