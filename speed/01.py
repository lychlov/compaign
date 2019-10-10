class Solution:
    # @param n, an integer
    # @return an integer
    pass


if __name__ == '__main__':
    in_file = open('.txt', 'r')
    out_file = open('01-out.txt', 'w')
    for line in in_file.readlines():
        
        line = line.strip()
        int_n = int(line)


        solution = Solution()
        # res = solution.reverseBits(int_n)
        # out_file.write(str(res)+'\r\n')
    pass
