class Solution:
    """
    @param n: the number of digit
    @return: the largest palindrome mod 1337
    """

    def largestPalindrome(self, n):
        # write your code here
        max_r = int('9' * n)
        min_r = 10 ** (n - 1) - 1
        palindromes = []
        for i in range(max_r, min_r, -1):
            if palindromes and max(palindromes) // i > max_r:
                break
            for j in range(max_r, min_r, -1):
                mul = i * j
                if self.isPalindrome(mul):
                    palindromes.append(mul)
                    break
        return max(palindromes) % 1337

    # faster way
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        half = 0
        while x > half:
            half = half * 10 + x % 10
            x //= 10
        return x == half or half / 10 == x


sol = Solution()
print(sol.isPalindrome(9009))
print(sol.largestPalindrome(5))
