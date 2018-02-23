class Solution:
    def minCostClimbingStairs(self, cost):
        #dp = [0] * (len(cost))
        #dp[0], dp[1] = cost[0], cost[1]

        #for i in range(2, len(cost)):
        #    dp[i] = min(dp[i-2] + cost[i], dp[i-1] + cost[i])

        #return min(dp[-2], dp[-1])
        a, b = 0, 0
        for i in range(2, len(cost) + 1):
            c = min(a + cost[i-2], b + cost[i-1])
            a, b = b, c
        return b

if __name__ == "__main__":
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    s = Solution()
    r = s.minCostClimbingStairs(cost)
    print(r)
