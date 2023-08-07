class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        s_new=''
        for i in range(len(s)-1,-1,-1):
            s_new +=  s[i]
        return True if s_new == s else False

x = Solution()
print(x.isPalindrome(-121))



