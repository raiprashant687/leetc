"""leet code solutions for substring with max length"""
from collections import deque
c= 'abcdabdcnr'
def abc(str_1):
    d = []
    s = deque(d)
    #print(len(s))
    max_1 = 0
    j = 0
    for i in range(len(str_1)):
        if str_1[i] not in s:
            s.append(str_1[i])
        else:
            while str_1[i] in s:
                s.popleft()
                j = j + 1
            s.append(str_1[i])


        max_1 = max(max_1,len(s))

    return(max_1)

print(abc(c))
