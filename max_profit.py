class Solution(object):
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    @staticmethod
    def maxProfit(prices):
        # write your code here
        profit = 0
        for i in range(len(prices)-1):
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]
        return profit


if __name__ == '__main__':
    prices = [2, 1, 2, 0, 1]
    print(Solution.maxProfit(prices))
