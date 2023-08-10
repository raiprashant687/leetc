class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while len(nums1)!=m:
            nums1.pop()
        for nu in nums2:
            nums1.append(nu)
        nums1.sort()
        return nums1

x=Solution()
print(x.merge([1,2,3,0,0,0],3,[2,5,6],3))