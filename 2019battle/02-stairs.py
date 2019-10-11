import networkx as nx


class Solution:
    def climb_stair_2(self, n):
        paths = {1: 1,
                 2: 2,
                 3: 4,
                 4: 8,
                 5: 16,
                 6: 32}
        for i in range(7, 101):
            paths[i] = 0
            for j in range(1, 7):
                paths[i] += paths[i - j]
        return paths

    def climb_stair(self, n):
        g = nx.DiGraph()
        edges = []
        for i in range(0, n):
            for j in range(1, 7):
                if i + j <= n:
                    edges.append([i, i + j])
        g.add_edges_from(edges)
        # print(edges)
        for i in range(1, 10):
            print(i, len(list(nx.all_simple_paths(g, 0, i))))
        # return len(list(nx.all_simple_paths(g, 0, n)))


if __name__ == '__main__':
    sol = Solution()
    paths = sol.climb_stair_2(100)

    path_to_file = r'/Users/zhikuncheng/PycharmProjects/2019battle' + '/{}.txt'
    with open(path_to_file.format('02-in'), 'r') as in_file:
        with open(path_to_file.format('02-out'), 'w', encoding='utf-8') as out_file:
            paths = sol.climb_stair_2(100)
            for i in range(1, 101):
                result = paths[i]
                out_file.write("{}\n".format(result))
