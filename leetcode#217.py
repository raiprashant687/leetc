class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        m = set(nums)
        if len(m) < len(nums):
            return True
        else:
            return False


x=Solution()
print(x.containsDuplicate([1,2,3,4,1]))