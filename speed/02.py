class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        n, m = len(matrix), len(matrix[0])
        pacific = set()
        atlantic = set()
        ans = []

        def dfs(matrix, visited, i, j):
            visited |= {(i, j)}
            for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and (ni, nj) not in visited:
                    if matrix[ni][nj] >= matrix[i][j]:
                        dfs(matrix, visited, ni, nj)

        for i in range(n):
            dfs(matrix, pacific, i, 0)
            dfs(matrix, atlantic, i, m - 1)
        for j in range(m):
            dfs(matrix, pacific, 0, j)
            dfs(matrix, atlantic, n - 1, j)
        return list(pacific & atlantic)


if __name__ == '__main__':
    in_file = open('water.txt', 'r')
    out_file = open('02-water-out.txt', 'w')
    matrix = []
    for line in in_file.readlines():
        line = line.strip()
        if line != '---' and line:
            digs = line.split(' ')
            matrix.append(digs)
        else:
            solution = Solution()
            res = solution.pacificAtlantic(matrix)
            matrix = []
            out_file.write(str(len(res)) + '\r\n')
    pass
