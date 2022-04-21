n,k= map(int,input().split()) 
expensive = []
for i in range(n):
    wishes= list(map(int,input().split()) )
    wishes.sort()
    m= wishes[-1]
    expensive.append(m)
expensive.sort() 
print(sum(expensive[0:k]))