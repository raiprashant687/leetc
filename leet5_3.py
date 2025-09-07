class Solution:
    def maxProfit(self, prices):
        max_1 = 0
        i = 0
        for i,j in enumerate(range(i+1,len(prices))):
            m = prices[j]-prices[i]
            max_1 = max(m, max_1)
            print(i,j)
        print(i)
        return max(max_1,0)

x = Solution()
print(x.maxProfit([7,1,5,3,6,4]))

