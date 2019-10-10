from collections import deque


class Solution(object):
    def ladderLength(self, begin, end, routes):
        """
        :type begin: str
        :type end: str
        :type routes: Set[str]
        :rtype: int
        """

        def getNbrs(src, dest, routes):
            res = []
            for route in routes:
                if src in route or dest in route:
                    yield route
        for route in routes:
            if begin in route:
                queue = deque(route)
        length = 0
        while queue:
            length += 1
            for k in range(0, len(queue)):
                top = queue.popleft()
                for station in top:
                    for nbr in getNbrs(station, end, routes):
                        routes.remove(nbr)
                        if nbr == end:
                            return length + 1
                        queue.append(nbr)
        return 0

if __name__ == '__main__':
    in_file = open('bus.txt', 'r')
    out_file = open('03-bus-out.txt', 'w')
    routes = []
    s, t = None, None
    for line in in_file.readlines():
        line = line.strip()
        if '=' not in line:
            routes.append(line.split(','))
        else:
            if 'S' in line:
                s = int(line.split('=')[-1])
            else:
                t = int(line.split('=')[-1])
        if s and t:
            solution = Solution()
            res = solution.ladderLength( str(s), str(t), routes)
            routes = []
            s, t = None, None
            out_file.write(str(res) + '\r\n')
    pass
