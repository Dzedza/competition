a,b,h = list(map(int,input().split()))

curr=0
i=0
step=0
while curr<h:
    if i%2==1:
        curr=curr-b
    if i%2==0:
        curr=curr+a
        step+=1
    i+=1

print(step)