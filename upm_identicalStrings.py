def sortStr(s):
    if len(s)==1:
        return s
    elif len(s)==3:
        return ''.join(sorted(s))
    a=int(len(s)/3)
    split_s=[s[0:a],s[a:2*a],s[2*a:3*a]]
    split_s=list(map(sortStr,split_s))
    split_s.sort()
    return ''.join(split_s)

n=int(input())
while n>0:
    str1=sortStr(input().strip())
    str2=sortStr(input().strip())
    if str1==str2:
        print("enaka")
    else:
        print("razlicna")
    n-=1