def get_int_list(ints):
    temp_list = ints.strip().split(' ')
    return list(filter(lambda x: x != 0, [int(i) / 1024 for i in temp_list]))

    pass


if __name__ == '__main__':
    with open(r'/Users/zhikuncheng/devspace/0828/04/in.txt', 'r') as in_str:
        with open(r'/Users/zhikuncheng/devspace/0828/04/out.txt', 'w', encoding='utf-8') as out_file:
            for ints in in_str.readlines():
                int_list = get_int_list(ints)
                int_list.sort()
                length = len(int_list)
                half = int(sum(int_list) / 2)
                searching = [[0 for i in range(half)] for j in range(length)]
                searching[length - 1][half - 1] = 0
                for i in range(length):
                    for j in range(half):
                        if int_list[i]<=j:
                            searching[i][j]=int_list[i]
                            
                print(length)
        pass
