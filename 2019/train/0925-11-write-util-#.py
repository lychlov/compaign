path_to_file = '{}.txt'
with open(path_to_file.format('out'), 'w', encoding='utf-8') as out_file:
    while True:
        in_str = input()
        if in_str is '#':
            break
        else:
            out_file.write('%s' % in_str)
