def triangle(n):
    return int((n*(n+1))/2)

pyramids=[0]
for i in range(1,600001):
    pyramids.append(triangle(i)+pyramids[-1])

c=int(input())
while c>0:
    print(pyramids[int(input())])
    c-=1