class Solution(object):
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """

    @staticmethod
    def woodCut(L, k):
        # write your code here

        max_cut=max(L)

        while max_cut > 0:
            count = 0
            for i in range(len(L)):
                count += L[i] // max_cut
            if count >= k:
                break
            max_cut -= 1
        return max_cut
        pass

if __name__ == '__main__':
    print(Solution.woodCut([232, 124, 456], 7))
    pass