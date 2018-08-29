if __name__ == '__main__':
    with open(r'/Users/zhikuncheng/devspace/0828/01/in.txt', 'r') as in_str:
        with open(r'/Users/zhikuncheng/devspace/0828/01/out.txt', 'w', encoding='utf-8') as out_file:

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
