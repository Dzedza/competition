n=int(input())
a,b=map(int,input().split())
a=a-b
lb=0
ub=1
possible=True
for i in range(n-1):
    if not possible:
        break
    a1,b1=map(int,input().split())
    a1=a1-b1
    d1,d2=a-a1,b1-b
    if a1<a:
        lb=max(lb,d2/d1)
    elif a1>a:
        ub=min(ub,d2/d1)
    elif d2>0:
        possible=False

if not possible or ub<lb:
    print("Slabe metrike")
else:    
    x=(lb+ub)/2
    print(x,1-x)