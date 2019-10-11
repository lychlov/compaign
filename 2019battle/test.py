

if __name__ == '__main__':
    path_to_file = r'/Users/zhikuncheng/PycharmProjects/2019battle' + '/{}.txt'
    with open(path_to_file.format('test-in'), 'r') as in_file:
        with open(path_to_file.format('out'), 'w', encoding='utf-8') as out_file:
            while in_file.readable():
                in_line = in_file.readline().strip()
                if not in_line:
                    break
                result = '10'
                out_file.write("{}\n".format(result))
