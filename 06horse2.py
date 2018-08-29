def run_horse(start, end):
    start_used = {start}
    end_used = {end}
    start_paths = [[start]]
    end_paths = [[end]]
    step_start = 0
    step_end = 0
    while True:
        if len(start_used) <= len(end_used):
            step_start += 1
            # start_used = move(start_used)
            new_pos, start_used = move_with_path(start_used)
            start_paths.append(new_pos)
        else:
            new_pos, end_used = move_with_path(end_used)
            # end_used = move(end_used)
            end_paths.append(new_pos)
            step_end += 1
        union = set(start_used) & set(end_used)
        if len(union) >= 1:
            mid_pos = union.pop()
            start_path = find_path(start_paths, mid_pos)
            end_path = find_path(end_paths, mid_pos)
            total_path = [start] + start_path[::-1] + end_path[1:] + [end]
            return step_start + step_end, total_path


def find_path(paths, target_pos):
    paths.pop(-1)
    result = [target_pos]
    while len(paths) > 1:
        path = paths.pop(-1)
        for i in range(len(move_x)):
            x = target_pos[0] + move_x[i]
            y = target_pos[1] + move_y[i]
            if (x, y) in path:
                target_pos = (x, y)
                result.append(target_pos)
                break
    return result
    pass


def move_with_path(used):
    new_pos_list = set()
    temp = used.copy()
    for pos in used:
        for i in range(len(move_x)):
            x = pos[0] + move_x[i]
            y = pos[1] + move_y[i]
            if 0 <= x <= 199 and 0 <= y <= 199 and (x, y) not in used:
                new_pos_list.add((x, y))
                temp.add((x, y))
    return new_pos_list, temp


def move(used):
    temp = used.copy()
    for pos in used:
        for i in range(len(move_x)):
            x = pos[0] + move_x[i]
            y = pos[1] + move_y[i]
            if 0 <= x <= 199 and 0 <= y <= 199:
                temp.add((x, y))
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

                step, step1 = run_horse(start, end)
                out_str = "%s " % step
                for pos in step1:
                    out_str += '(%s,%s) ' % (pos[0], pos[1])
                out_str = out_str.strip() + '\n'
                out_file.write(out_str)
                print(out_str)
