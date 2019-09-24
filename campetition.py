class Solution(object):

    def find_island(self, grid_temp):
        fold = set()
        searched = set()

        while len(fold) + len(searched) < len(grid_temp):
            seed = grid_temp.pop()
            for pos in grid_temp:
                if pos[0]-1<=seed[0]<=pos[0]+1 or pos[1]-1<=seed[1]<=pos[1]+1:
                    fold.add(pos)

        for origin in grid_temp:
            for pos_set in islands:
                temp_pos = []
                for pos in pos_set:
                    if pos[0] - 1 <= origin[0] <= pos[0] + 1 or pos[1] - 1 <= origin[1] <= pos[1] + 1:
                        temp_pos.append(origin)

                pos_set = temp_pos + pos_set
            new_island = []
            new_island.append(origin)
            islands.append(new_island)
        return len(islands)

    pass


if __name__ == '__main__':
    with open('islands.txt', 'r')as in_file:
        with open('out-is.txt', 'w') as out_file:
            grids = []
            positions = set()
            line_count = 0
            for line in in_file.readlines():
                line = line.strip()
                if '-' in line:
                    grids.append(positions)
                    positions = set()
                    line_count = 0
                else:
                    for i in range(len(line)):
                        if line[i] == '1':
                            positions.add((line_count, i))
                # out_file.write('%s\r\n'%cout)
                line_count += 1
            for grid in grids:
                print(grid)
    pass
