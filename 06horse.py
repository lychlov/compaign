def run_horse(start, end):
    paths_start = [[start]]
    paths_end = [[end]]

    while True:
        if len(paths_start) <= len(paths_end):
            paths = paths_start
            targets = paths_end
        else:
            paths = paths_end
            targets = paths_start
        temp = []
        for path in paths:
            moved_paths = move(path)
            for moved in moved_paths:
                for target in targets:
                    # if target[-1] in moved:
                    if len(set(target) & set(moved)) >= 1:
                        return moved, target
                temp.append(moved)
        if len(paths_start) <= len(paths_end):
            paths_start = temp.copy()
        else:
            paths_end = temp.copy()


def move(path):
    temp = []
    for i in range(len(move_x)):
        temp_path = path.copy()
        x = path[-1][0] + move_x[i]
        y = path[-1][1] + move_y[i]
        if 0 <= x <= 199 and 0 <= y <= 199 and (x, y) not in path:
            temp_path.append((x, y))
            temp.append(temp_path)
    return temp


if __name__ == '__main__':
    with open(r'/Users/zhikuncheng/devspace/0828/06/in.txt', 'r') as in_str:
        with open(r'/Users/zhikuncheng/devspace/0828/06/out.txt', 'w', encoding='utf-8') as out_file:
            move_x = [1, 1, -1, -1, 2, 2, -2, -2]
            move_y = [2, -2, 2, -2, 1, -1, 1, -1]
            for position in in_str.readlines():
                step = 0
                pos = position.split(' ')
                start = (int(pos[0]), int(pos[1]))
                end = (int(pos[2]), int(pos[3]))

                step, step2 = run_horse(start, end)
                print(step, step2)
