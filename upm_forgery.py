def check(a,b):
    if a==0:
        return False
    if a==1 and b>0:
        return False
    if a>b+1:
        return False
    if a%2==b%2:
        return False
    return True

t=int(input())
while t>0:
    x,y=map(int,input().strip().split())
    res=check(x,y)
    if res:
        print("DA")
    else:
        print("NE")
    t-=1