n,m= map(int,input().split())
cands= [i for i in range(1,m+1)]

def digit_sum(x):
    x=[int(c) for c in str(x)]
    return sum(x)


cands=list(map(digit_sum,cands))
cands=[i for i in cands if i<=n]

def solve(s):
    x = len(s)
    count=0
    for i in range(1 << x):
        su=sum([s[j] for j in range(x) if (i & (1 << j))])
        if su==n:
            count=(count+1)%1000037
    return count

print(solve(cands))