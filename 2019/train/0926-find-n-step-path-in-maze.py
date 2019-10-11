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


def find_all_path_with_networkx(edges, start, end, time):
    import networkx as nx
    g = nx.DiGraph()
    g.add_edges_from(edges)
    return bool(list(nx.all_simple_paths(g, start, end, time)))


def find_all_path_with_stack(graph, start, target, time):
    if time < 1:
        return None
    paths = []
    visited = [start]
    stack = [iter(graph[start])]
    while stack:
        children = stack[-1]
        child = next(children, None)
        if child is None:
            stack.pop()
            visited.pop()
        elif len(visited) < time:
            if child == target:
                paths.append(visited + [target])
            elif child not in visited:
                visited.append(child)
                stack.append(iter(graph[child]))
        else:  # len(visited) == cutoff:
            if child == target or target in children:
                paths.append(visited + [target])
            stack.pop()
            visited.pop()
    return paths


def get_maze_edges(maze, rows, columns):
    edges = []
    for row in range(rows):
        for col in range(columns):
            if maze[row][col] is 1:
                if get_positon(maze, row + 1, col): edges.append(((row, col), (row + 1, col)))
                if get_positon(maze, row - 1, col): edges.append(((row, col), (row - 1, col)))
                if get_positon(maze, row, col + 1): edges.append(((row, col), (row, col + 1)))
                if get_positon(maze, row, col - 1): edges.append(((row, col), (row, col - 1)))
    return edges


def _all_simple_paths_graph(G, source, target, cutoff=None):
    if cutoff < 1:
        return
    visited = [source]
    stack = [iter(G[source])]
    while stack:
        children = stack[-1]
        child = next(children, None)
        if child is None:
            stack.pop()
            visited.pop()
        elif len(visited) < cutoff:
            if child == target:
                yield visited + [target]
            elif child not in visited:
                visited.append(child)
                stack.append(iter(G[child]))
        else:  # len(visited) == cutoff:
            if child == target or target in children:
                yield visited + [target]
            stack.pop()
            visited.pop()


def get_statics(statics: str):
    statics = statics.split(' ')
    return int(statics[0]), int(statics[1]), int(statics[2])


if __name__ == '__main__':
    path_to_file = r'/Users/zhikuncheng/PycharmProjects/compaign/2019/train/0926-maze-{}.txt'
    with open(path_to_file.format('in'), 'r') as in_str:
        with open(path_to_file.format('out'), 'w', encoding='utf-8') as out_file:
            while in_str.readable():
                statics = in_str.readline().strip()
                rows, columns, time = get_statics(statics)
                if rows == 0:
                    break
                maze = []
                print(maze)
                start, end = (0, 0)
                for row in range(rows):
                    row_str = in_str.readline().strip()
                    row_count = []
                    for col in range(columns):
                        if row_str[col] is "S":
                            start = (row, col)
                            row_count.append(1)
                        elif row_str[col] is "D":
                            end = (row, col)
                            row_count.append(1)
                        elif row_str[col] is "X":
                            row_count.append(0)
                        else:
                            row_count.append(1)
                    maze.append(row_count)
                print(maze)
                maze_edges = get_maze_edges(maze, rows, columns)
                maze_graph = draw_graph_with_edges(maze_edges)
                result = find_all_path_with_networkx(maze_edges, start, end, time)

                result = find_all_path_with_stack(maze_graph, start, end, time)

                out_file.write("{}\n".format(bool(result)))
