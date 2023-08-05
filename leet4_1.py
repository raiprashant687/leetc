from collections import deque
s = '([)]'
def st(s):
    s_d = deque(s)
    if len(s)%2!=0:
        q = False
    if len(s)%2==0:
        while(len(s_d)>0):
            if s_d[0] == '(':
                if s_d[-1]==')':
                    s_d.pop()
                    s_d.popleft()
                    continue
                else:
                    q = False
            elif s_d[0] == '{':
                if s_d[-1]=='}':
                    s_d.pop()
                    s_d.popleft()
                    continue
                else:
                    q = False
            elif s_d[0] == '[':
                if s_d[-1]==']':
                    s_d.pop()
                    s_d.popleft()
                    continue
                else:
                    q = False

    if len(s_d)==0:
        return True
    else: return False

print(st(s))