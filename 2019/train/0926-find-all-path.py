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


def find_all_path_with_recursion(graph, start, end, path: list = []):
    path = path + [start]  # 为什么path.append(start)不行
    if start == end:
        return [path]
    paths = []
    for step in graph[start]:
        if step not in path:
            next_paths = find_all_path_with_recursion(graph, step, end, path)
            for p in next_paths:
                paths.append(p)
    return paths
    pass


def find_shortest_path(edges, start, end):
    import networkx as nx
    g = nx.DiGraph()
    g.add_edges_from(edges)
    return list(nx.all_shortest_paths(g, start, end))
    pass


def find_all_paths_with_stack(graph, start, target):
    paths = []
    visited = [start]
    stack = [iter(graph[start])]
    while stack:
        children = stack[-1]
        child = next(children, None)
        if child is None:
            stack.pop()
            visited.pop()
        else:
            if child == target:
                paths.append(visited + [target])
            elif child not in visited:
                visited.append(child)
                stack.append(iter(graph[child]))
    return paths


def find_all_paths_with_stack_2(graph, start, target):
    paths = []
    visited = [start]
    stack = [iter(graph[start])]  # 使用ITER解决了深浅拷贝问题
    while stack:
        children = stack[-1]
        child = next(children, None)
        if child is None:
            stack.pop()
            visited.pop()
        else:
            if child == target:
                paths.append(visited + [target])
            elif child not in visited:
                visited.append(child)
                stack.append(iter(graph[child]))
    return paths


edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D'),
         ('D', 'C'), ('E', 'F'), ('F', 'C')]
graph_to = draw_graph_with_edges(edges)
print(find_all_path_with_networkx(edges, 'A', 'D'))
print(find_all_path_with_recursion(graph_to, "A", "D"))
print(find_all_paths_with_stack_2(graph_to, "A", "D"))
