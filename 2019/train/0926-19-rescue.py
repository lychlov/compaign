# 这个题和狗的问题一样，求出求出所有路径后，警卫的节点权值为2，其他为1，求所有路径的权值，取最小的。
# 这个问题是在途中找出指定长度的路径，使用find_all_path可解
def get_positon(maze, x, y):
    if x < 0 or y < 0:
        return None
    try:
        return maze[x][y]
    except:
        return None


def draw_graph_with_edges(edges):
    graph = {}
    for edge in edges:
        if edge[0] in graph.keys():
            graph[edge[0]].append(edge[1])
        else:
            graph[edge[0]] = [edge[1]]
    return graph


def find_all_path_with_networkx(edges, start, end):
    import networkx as nx
    g = nx.DiGraph()
    g.add_edges_from(edges)
    return list(nx.all_simple_paths(g, start, end))


def get_maze_edges(maze, rows, columns):
    edges = []
    for row in range(rows):
        for col in range(columns):
            if maze[row][col]:
                if get_positon(maze, row + 1, col): edges.append(((row, col), (row + 1, col)))
                if get_positon(maze, row - 1, col): edges.append(((row, col), (row - 1, col)))
                if get_positon(maze, row, col + 1): edges.append(((row, col), (row, col + 1)))
                if get_positon(maze, row, col - 1): edges.append(((row, col), (row, col - 1)))
    return edges


def get_statics(statics: str):
    statics = statics.split(' ')
    return int(statics[0]), int(statics[1])


if __name__ == '__main__':
    path_to_file = r'/Users/zhikuncheng/PycharmProjects/compaign/2019/train/0926-19-rescue-{}.txt'
    with open(path_to_file.format('in'), 'r') as in_str:
        with open(path_to_file.format('out'), 'w', encoding='utf-8') as out_file:
            while in_str.readable():
                statics = in_str.readline().strip()
                rows, columns = get_statics(statics)
                if rows == 0:
                    break
                maze = []
                print(maze)
                start, end = (0, 0)
                for row in range(rows):
                    row_str = in_str.readline().strip()
                    row_count = []
                    for col in range(columns):
                        if row_str[col] is "r":
                            start = (row, col)
                            row_count.append(1)
                        elif row_str[col] is "a":
                            end = (row, col)
                            row_count.append(1)
                        elif row_str[col] is "#":
                            row_count.append(0)
                        elif row_str[col] is 'x':
                            row_count.append(2)
                        else:
                            row_count.append(1)
                    maze.append(row_count)
                print(maze)
                maze_edges = get_maze_edges(maze, rows, columns)
                paths = find_all_path_with_networkx(maze_edges, start, end)
                costs = []
                path_map = {}
                if paths:
                    for path in paths:
                        cost = sum([maze[i[0]][i[1]] for i in path])
                        costs.append(cost)
                    # 自己的第一步不算
                    result = min(costs) - 1
                else:
                    result = 'Poor ANGEL has to stay in the prison all his life.'
                out_file.write("{}\n".format(result))
