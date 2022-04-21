from sys import stdin

items=input().strip().split(", ")

lines=[i.strip() for i in stdin.readlines()]


stores=[]
available=[]
prices=[]
i=0
j=-1

while i < len(lines):
    if lines[i]=="":
        stores.append(lines[i+1])
        available.append([])
        prices.append([])
        j+=1
        i+=2
    else:
        thing,price=lines[i].rsplit(" ",1)
        available[j].append(thing)
        prices[j].append(float(price))
        i+=1

#print(stores)
#print(prices)

for item in items:
    for i in range(len(stores)):       
        if item not in available[i]:
            stores[i] = 0


available=[available[a] for a in range(len(available)) if stores[a]!=0]
prices=[prices[p] for p in range(len(prices)) if stores[p]!=0]
stores=[stores[s] for s in range(len(stores)) if stores[s]!=0]
money = [0 for i in range(len(stores))]

for i in range(len(stores)):
    budget = 0
    for item in items:
        budget+=prices[i][available[i].index(item)]
    money[i] = budget

best_price = min(money)
best_store = stores[money.index(best_price)]

print(best_store + " " + str(round(best_price,2)))