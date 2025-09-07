
#start from 1
# then check ifi and j are not equal if true then add them to result
# increment the j counter to j+1 check for j if it exists in result if not
# then add j to result and update the result if yes then update m = presentone
# again start the same process
s='abcdbcdnr'
def chk(s):
    max_1 = 0
    if len(s)==1:
        return len(s)
    elif len(s)==0:
        return len(s)
    else:
        for i in range(len(s)):
            str_1 = ''
            #print(str_1)
            for j in range(i+1,len(s)):
                if s[i] not in s[j]:
                    str_1 = str_1+s[j]
                elif s[i]==s[j]:
                    str_1 = s[j]
                max_1 = max(max_1, len(str_1))
                #print(max_1)
        return(max_1)

print(chk(s))
# #1st ieteration:- s= abcdabcdnr
# str-1= ab,s[i]=a,s[j]=b,max_1=2
