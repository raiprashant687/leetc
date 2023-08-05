
class Solution:
    def isValid(self, s: str) -> bool:

        #print(s_new)
        m = 0
        for i in range(len(s)):
            if s[i] == '(':
                m = m -1

            if s[i] == '{':
                m = m-2

            if s[i]=='[':
                m = m-3

            if s[i] in ')':
                m = m+1

            if s[i]=='}':
                m = m+2

            if s[i]==']':
                m = m+3


        if m ==0:
            return True
        else:
            return False

x = Solution()
print(x.isValid('[[]]}'))