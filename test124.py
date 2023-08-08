"""program showing the faster execution when in is used in comparison to in range"""

import timeit


k = """
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
for num in matrix:
    for n in num:
        pass
"""


m = """
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

for i in range(len(matrix)):
    for k in range(len(matrix[i])):
        pass
"""
print(timeit.timeit(stmt=k,number=1000))
print(timeit.timeit(stmt=m,number=1000))