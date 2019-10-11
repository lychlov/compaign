import networkx as nx


class solution():

    def __init__(self, maze, monsters_o={}, start=(0, 0)):
        self.maze = maze
        self.monsters = {}
        self.start = start
        index = 1
        sort = list(monsters_o.keys())
        sort.sort()
        for key in sort:
            self.monsters[key] = monsters_o[key]
            if key == 99999:
                pass
            else:
                if key != index:
                    self.monsters = None
                    temp = list(monsters_o.keys())
                    temp.sort()
                    print(temp)
                    break
            index += 1
        self.g = nx.DiGraph()
        self.g.add_edges_from(self.get_maze_edges())

    def run(self):
        if self.monsters is None:
            return '0'
        path = []
        tem_start = self.start
        while self.monsters:
            sort = list(self.monsters.keys())
            sort.sort()
            monster = self.monsters.pop(sort[0])
            edges = []
            row = monster[0]
            col = monster[1]
            self.maze[row][col] = 1
            self.g = nx.DiGraph()
            self.g.add_edges_from(self.get_maze_edges())
            try:
                steps = nx.all_shortest_paths(self.g, tem_start, monster)
                for step in steps:
                    path += step[1:]
                    break
            except:
                steps = []
                return '0'
            tem_start = monster
        return path
        # self.monsters =

    def get_positon(self, x, y):
        if x < 0 or y < 0:
            return None
        try:
            return self.maze[x][y]
        except:
            return None

    def get_maze_edges(self):
        edges = []
        for row in range(len(self.maze)):
            for col in range(len(self.maze[0])):
                if self.maze[row][col] is 1:
                    if self.get_positon(row + 1, col): edges.append(((row, col), (row + 1, col)))
                    if self.get_positon(row - 1, col): edges.append(((row, col), (row - 1, col)))
                    if self.get_positon(row, col + 1): edges.append(((row, col), (row, col + 1)))
                    if self.get_positon(row, col - 1): edges.append(((row, col), (row, col - 1)))
        return edges


if __name__ == '__main__':
    path_to_file = r'/Users/zhikuncheng/PycharmProjects/2019battle' + '/{}.txt'
    with open(path_to_file.format('03-maze-in'), 'r') as in_file:
        with open(path_to_file.format('03-maze-out'), 'w', encoding='utf-8') as out_file:
            while in_file.readable():
                in_line = in_file.readline().strip()
                print(in_line)
                if not in_line:
                    break
                if in_line == '----':
                    continue
                n = int(in_line.split(' ')[0])
                m = int(in_line.split(' ')[1])
                start = (0, 0)
                target = (0, 0)
                origin_maze = []
                monsters = {}
                for i in range(0, n):
                    origin_maze.append([0] * m)
                    row = in_file.readline().strip()
                    row = row.split(' ')
                    for j in range(0, m):
                        if row[j] == '-1':
                            origin_maze[i][j] = 0
                        elif row[j] == '0':
                            origin_maze[i][j] = 1
                        elif row[j] == '-99':
                            origin_maze[i][j] = 1
                            monsters[99999] = (i, j)
                            target = (i, j)
                        else:
                            origin_maze[i][j] = 0
                            if int(row[j]) in monsters.keys():
                                print('同样怪物等级')
                            monsters[int(row[j])] = (i, j)
                sol = solution(origin_maze, monsters, start)
                result = sol.run()
                if result == '0':
                    result = -1
                else:
                    result = len(result)
                out_file.write("{}\n".format(result))
