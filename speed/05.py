class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = j = 0
        lenS = len(s)
        lenP = len(p)
        lastMatchPos = 0
        lastStarPos = -1
        while i < len(s):
            if j < lenP and p[j] in (s[i], "?"):
                i += 1
                j += 1
            elif j < lenP and p[j] == "*":
                lastMatchPos = i
                lastStarPos = j
                j += 1
            elif lastStarPos > -1:
                i = lastMatchPos + 1
                lastMatchPos += 1
                j = lastStarPos + 1
            else:
                return False
        while j < lenP and p[j] == "*":
            j += 1
        return 'true' if j == lenP else 'false'

if __name__ == '__main__':
    in_file = open('match.txt', 'r')
    out_file = open('05-match-out.txt', 'w')
    s, reg = '', ''
    for line in in_file.readlines():
        line = line.strip()
        if line != '---' and line:
            if s:
                reg = line
            else:
                s = line
        if s and reg:
            solution = Solution()
            res = solution.isMatch(s, reg)
            s,reg='',''
            out_file.write(str(res) + '\r\n')
    pass
