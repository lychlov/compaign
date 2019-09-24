def get_all_numbers_1():
    digs = [1, 2, 3, 4]
    all_numbers = [100 * i + 10 * j + k for i in digs for j in digs for k in digs]
    return len(all_numbers), all_numbers


def get_all_numbers_2():
    __, alls = get_all_numbers_1()
    all_numbers = list(filter(lambda i: len(set([str(i)[0], str(i)[1], str(i)[2]])) == 3, alls))
    return len(all_numbers), all_numbers


