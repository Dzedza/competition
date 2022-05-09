import sys
 
n,m= map(int, sys.stdin.readline().split())
park= [c for c in sys.stdin.readline()]
 
placed=0
for i in range(m-1):
    if park[i]=='_' and park[i+1]=='_':
        placed+=1
    if placed==n:
        break
 
print(n-placed)
