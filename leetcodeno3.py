"""Given a string s, find the length of the longest
substring
 without repeating characters."""
s = 'abcdabcndra'
def substring(s):
    new = []
    m = ''
    result = {}
    for i in range(len(s)):
        if s[i] not in m:
            m = m+ s[i]
        elif s[i] in m:
            new.append(len(m))
            m = ''
            m = m + s[i]
            continue
    return max(new)

print(substring(s))



