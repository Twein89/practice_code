class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        low, profit = prices[0], 0
        for n in prices:
            low = n if n < low else low
            p = n - low
            profit = p if p > profit else profit
        return profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    s = Solution()
    r = s.maxProfit(prices)
    print(r)
