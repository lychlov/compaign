class Solution:
    """
    @param grid: a grid
    @param hits: some erasures order
    @return: an array representing the number of bricks that will drop after each erasure in sequence
    """

    def hitBricks(self, grid, hits):
        # Write your code here
        counts = []
        for hit in hits:
            x = hit[0]
            y = hit[1]
            count = 0
            while grid[x][y] == 1:
                grid[x][y] = 0
                count += 1
                y += 1
            counts.append(count - 1)
        return counts


sol = Solution()
print(sol.hitBricks([[1, 0, 0, 0], [1, 1, 1, 0]], [[1, 0]]))
