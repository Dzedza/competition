import sys
import math
input = sys.stdin.readline

def mile(l):
    s=0
    for call in l:
        s+=(math.floor(call/30)+1)*10
    return s

def juice(l):
    r=0
    for call in l:
        r+=(math.floor(call/60)+1)*15
    return r


t = int(input())
for i in range(t):
    n=int(input())
    calls = list(map(int,input().split()))
    j= juice(calls)
    m= mile(calls)
    if m<j:
        print("Case "+str(i+1)+": "+"Mile "+str(m))
    elif j<m:
        print("Case "+str(i+1)+": "+"Juice "+str(j))
    else:
        print("Case "+str(i+1)+": "+"Mile Juice "+str(m))