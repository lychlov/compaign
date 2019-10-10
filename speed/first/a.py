class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        mask = 1
        for _ in range(32):
            ans <<= 1
            if mask & n:
                ans |= 1
            n >>= 1
        return ans


if __name__ == '__main__':
    in_file = open('number.txt', 'r')
    out_file = open('1-number-anwser.txt', 'w')
    for line in in_file.readlines():
        line=line.strip()
        int_n = int(line)

        solution = Solution()
        res = solution.reverseBits(int_n)
        out_file.write(str(res)+'\r\n')
    pass
