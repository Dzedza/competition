import math
n,l= map(int,input().split())
squares=[i**2 for i in range(1,l+1)]
def count(m,k):
    if m>2:
        return 0
    if m==1:
        cnt=0
        for i in range(2,k+1):
            cnt= cnt+math.floor(i/2)
        return cnt
    cnt=0
    for i in range(2,l):
        for j in range(0,i):
            for k in range(0,j):
                if squares[j]+squares[k]==squares[i]:
                    cnt+=1
    return cnt
    
 
print(count(n,l))
