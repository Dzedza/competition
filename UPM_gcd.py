from math import gcd as gcd


def solve(n):
    if n==0 or n==1:
        return 1
    if n>1000:
        if n%4==1:
            return 2
        if n%4==2:
            return 1
        if n%4==3:
            return n+2
        if n%4==0:
            return 2*n+2
    curr=1
    for i in range(2,n+1):
        d= gcd(curr,i)
        if d==1:
            curr= curr+i+1
        else:
            curr= curr//d
    return curr



t= int(input())
ns= list(map(int,input().split()))
res= list(map(solve,ns))
print(" ".join(list(map(str,res))))