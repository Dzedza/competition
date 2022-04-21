import math

def reflect(x,y,a,b,c,d):
    dx=c-a
    dy=d-b
    p=(dx*dx-dy*dy)/(dx*dx+dy*dy)
    s=2*dx*dy/(dx*dx+dy*dy)
    x1=p*(x-a)+s*(y-b)+a
    y1=s*(x-a)-p*(y-b)+b
    return x1,y1

pts=[]
n=int(input())
for i in range(n):
    pts.append(tuple(map(int,input().split())))
m=int(input())
for i in range(m):
    task=input()
    if task[0]=="T":
        pts.append(tuple(map(int,task[2:].split())))
    elif task[0]=="Z":
        a,b,c,d=tuple(map(int,task[2:].split()))
        for j in range(len(pts)):
            pts[j]=tuple(reflect(pts[j][0],pts[j][1],a,b,c,d))
    else:
        j=int(task[2:])
        x,y=pts[j-1]
        print(x,y)
        