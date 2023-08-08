class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        count = 0
        for num in matrix:
            #print(num)
            for n in num:
                if n == target:
                    count = 1
                    break

        if count>0:
            return True
        else:
            return False





x=Solution()
print(x.searchMatrix([[1],[3]],3))