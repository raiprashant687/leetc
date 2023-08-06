#68ms run time
class Solution:
    def maxProfit(self, prices):
        min_1 = prices[0]
        max_1 = 0
        for i in range(1,len(prices)):
            min_1 = min(prices[i],min_1)

        m = prices.index(min_1)
        #print(m)
        if m == len(prices)-2:
            max_1 = prices[m+1]
        else:
            for j in range(m,len(prices)):
                max_1 = max(max_1,prices[j])

        if min_1 < max_1:
            return (max_1-min_1)
        else:
            return 0

x = Solution()
print(x.maxProfit([3,2,6,5,0,3]))

