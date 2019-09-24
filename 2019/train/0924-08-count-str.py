if __name__ == '__main__':
    path_to_file=r'/Users/zhikuncheng/PycharmProjects/compaign/2019/train/08_{}.txt'
    with open(path_to_file.format('in'), 'r') as in_str:
        with open(path_to_file.format('out'), 'w', encoding='utf-8') as out_file:

            for str in in_str.readlines():
                str=str.strip()
                eng_count = 0
                dig_count = 0
                space_count = 0
                other_count = 0
                for char in str:
                    if u'a' <= char <= u'z' or u'A' <= char <= u'Z':
                        eng_count += 1
                    elif u'0' <= char <= u'9':
                        dig_count += 1
                    elif char == u' ':
                        space_count += 1
                    else:
                        other_count += 1
                out_file.write('%s %s %s %s\n' % (eng_count, dig_count, space_count, other_count))
