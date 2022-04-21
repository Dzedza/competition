mess=input()
n=len(mess)
r=0
for i in range(1,n//2+2):
    if n%i==0 and i<=n/i:
        r=i
res=""
for i in range(r):
    for j in range(n):
        if j%r==i:
            res+=mess[j]
print(res)