if __name__ == '__main__':
    logic = [0, 0, 0, 0]
    for thief in ['a', 'b', 'c', 'd']:
        logic[0] = 1 if 'a' != thief else 0
        logic[1] = 1 if 'c' == thief else 0
        logic[2] = 1 if 'd' == thief else 0
        logic[3] = 1 if 'd' != thief else 0
        if sum(logic) == 3:
            print(thief)
