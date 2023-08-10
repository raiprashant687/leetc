class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ''
        for i in range(len(s)):
            if s[i].isupper():
                s_new = s_new + s[i].lower()
            elif s[i].islower():
                s_new = s_new + s[i]
            elif s[i].isalnum():
                s_new = s_new + s[i]
            else:
                continue
        #print(s_new[:],s_new[::-1])
        return True if s_new[:] == s_new[::-1] else False

x = Solution()
print(x.isPalindrome("A man, a plan, a canal: Panama"))


