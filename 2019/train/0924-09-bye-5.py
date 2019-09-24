def bye_5(n):
    circle = list(range(1, n + 1))
    bye = 0
    bye_count = 0
    while bye_count < len(circle) - 1:
        for i in range(len(circle)):
            if circle[i] != 0:
                if bye == 5:
                    bye = 1
                else:
                    bye += 1
                if bye == 5:
                    circle[i] = 0
                    bye_count += 1
    for i in circle:
        if i != 0:
            return i


if __name__ == '__main__':
    path_to_file = r'/Users/zhikuncheng/PycharmProjects/compaign/2019/train/09_{}.txt'
    with open(path_to_file.format('in'), 'r') as in_str:
        with open(path_to_file.format('out'), 'w', encoding='utf-8') as out_file:
            for total in in_str.readlines():
                total = int(total)
                result = bye_5(total)
                print(result)
                out_file.write('%s\n' % (result))
