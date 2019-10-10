class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = 0
        ans = 0
        bound = len(nums)
        while pos < len(nums) - 1:
            dis = nums[pos]
            farthest = posToFarthest = 0
            for i in range(pos + 1, min(pos + dis + 1, bound)):
                canReach = i + nums[i]
                if i == len(nums) - 1:
                    return ans + 1
                if canReach > farthest:
                    farthest = canReach
                    posToFarthest = i
            ans += 1
            pos = posToFarthest
        return ans


if __name__ == '__main__':
    in_file = open('jump.txt', 'r')
    out_file = open('5-jump-count.txt', 'w')
    for line in in_file.readlines():
        line = line.strip()
        array = line.split(',')
        array= [int(i) for i in array]
        solution = Solution()
        res = solution.jump(array)
        out_file.write(str(res)+'\r\n')

    pass
