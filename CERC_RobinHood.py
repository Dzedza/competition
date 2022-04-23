import sys
import heapq

n,k= map(int, sys.stdin.readline().strip().split())

bla= [-x for x in map(int, sys.stdin.readline().strip().split())]
rich=[[bla[i],i] for i in range(len(bla))]        
heapq.heapify(rich)
done=False

for i in range(k):
    cand=heapq.heappop(rich)
    if -cand[0]<=100:
        print('impossible')
        done=True
        break
    cand[0]=cand[0]+100
    heapq.heappush(rich,cand)

if not done:
    rich=[(i,-x) for (x,i) in rich]   
    rich.sort()
    rich=[x for (i,x) in rich]
    print(' '.join(map(str,rich)))
