#59ms but excceds time limit in some cases
class Solution:
    def maxProfit(self, prices):
        max_1 = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                m = prices[j]-prices[i]
                max_1 = max(m,max_1)
        return max(max_1,0)

x = Solution()
print(x.maxProfit([1,2,3,4,5,6]))

