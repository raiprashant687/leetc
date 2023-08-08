class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        count =0
        for i in range(10,n+1):
            s= str(i)
            j=''
            for k in range(len(s)):
                if s[k] not in j:
                    j=j+s[k]
                else:
                    count +=1
                    break
        return count

x=Solution()
print(x.numDupDigitsAtMostN(6718458))