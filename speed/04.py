# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         maxLen = 0
#         single = False
#         d = {}
#         for c in s:
#             d[c] = d.get(c, 0) + 1
#
#         for key in d:
#             if d[key] >= 2:
#                 count = d[key]
#                 left = d[key] % 2
#                 d[key] = left
#                 maxLen += count - left
#             if not single:
#                 if d[key] == 1:
#                     maxLen += 1
#                     single = True
#         return maxLen

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = right = 0
        n = len(s)
        for i in range(n - 1):
            if 2 * (n - i) + 1 < right - left + 1:
                break
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 2 > right - left:
                left = l + 1
                right = r - 1
            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 2 > right - left:
                left = l + 1
                right = r - 1
        return s[left:right + 1]

if __name__ == '__main__':
    in_file = open('palindrome.txt', 'r')
    out_file = open('04-palindrome.txt', 'w')
    for line in in_file.readlines():
        line = line.strip()
        if line != '---':
            solution = Solution()
            res = solution.longestPalindrome(line)
            out_file.write(str(len(res))+'\r\n')
    pass
