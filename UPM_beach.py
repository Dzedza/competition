import sys
sys.setrecursionlimit(500000)
 
n,m= map(int,input().split())
adj= [[] for i in range(n+1)]
for i in range(m):
    a,b= map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
zus=[1]
mm=[]
done= [False for i in range(n+1)]
def fill(x):
    done[x]=True
    if len(zus)+len(mm)==n:
        return
    for num in adj[x]:
        if x in zus:
            if num not in mm:
                mm.append(num)
        else:
            if num not in zus:
                zus.append(num)
    for num in adj[x]:
        if not done[num]:
            fill(num)
fill(1)
l=list(set(zus))
l.sort()
l=list(map(str,l))
print(' '.join(l))
