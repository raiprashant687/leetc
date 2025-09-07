#66ms run time
class Solution:
    def maxProfit(self, prices):
        min_1 = prices[0]
        max_p = 0
        for i in range(1,len(prices)):
            min_1 = min(prices[i],min_1)
            max_p = max(max_p,prices[i]-min_1)
        return max_p

x = Solution()
print(x.maxProfit([3,2,6,5,0,3]))

