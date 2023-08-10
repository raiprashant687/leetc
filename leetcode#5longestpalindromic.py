# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         result = []
#         max_length = 0
#         for i in range(len(s)):
#             if s[:]==s[-1:]:
#                 result.append()
n =7
l = [1,2,3,4,5,6,7]

m = int(n/2)
i = m
j = m 

for i,j in zip(range(0),range(len(l))):
    print(l[i],l[j])