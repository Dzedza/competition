import  math

p,a,b,c,d,n = list(map(int,input().split()))

def price(k):
    return p*(math.sin(a*k+b)+math.cos(c*k+d)+2)

prices = [price(i+1) for i in range(n)]

biggestDiff=0
biggestElt=0
for i in range(n):
    biggestDiff=max(biggestDiff,biggestElt-prices[i])
    biggestElt=max(biggestElt,prices[i])

print(biggestDiff)