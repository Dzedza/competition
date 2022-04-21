def stut(s):
    if len(s)==1:
        return False
    for i in range(1,len(s)):
        if s[i]==s[0]:
            subs=s[0:i]
            break
    if i==len(s)-1:
        return False
    if len(s)<=i+len(subs):
        return False
    if subs==s[i:i+len(subs)]:
        return True
    return False

t=int(input())

while t>0:
    check=stut(input().strip())
    if check:
        print('da')
    else:
        print('ne')
    t-=1

