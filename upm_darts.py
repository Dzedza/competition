import math as m

pts=[6,13,13,4,4,18,18,1,1,20,20,5,5,12,12,
9,9,14,14,11,11,8,8,16,16,7,7,19,19,3,3,17,17,2,2,15,15,10,10,6]

def tan(x,y):
    tg=m.degrees(m.atan2(y,x))
    if tg<0:
        tg+=360
    return tg

def points(x,y):
    squares=x*x + y*y
    if squares>170*170:
        return 0
    if squares<6.35*6.35:
        return 50
    if squares<15.9*15.9:
        return 25
    alpha=tan(x,y)
    p=pts[m.floor(alpha/9)]
    if squares<107*107 and squares>97.4*97.4:
        p*=3
    if squares>160.4*160.4:
        p*=2
    return p

t=int(input())
while t>0:
    n=int(input())
    score=0
    for j in range(n):
        a,b=map(float,input().strip().split())
        score+=points(a,b)
    print(score)
    t-=1