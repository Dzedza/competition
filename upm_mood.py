def calc(msg):
    score=0
    j=1
    while j<len(msg):
        if msg[j-1]==":" and msg[j]==")":
            k=j
            while msg[k]==")":
                score+=1
                k+=1
                if k>=len(msg):
                    break
            j=k
        elif msg[j-1]==":" and msg[j]=="(":
            k=j
            while msg[k]=="(":
                score-=1
                k+=1
                if k>=len(msg):
                    break
            j=k
        else:
            j+=1
    return score

m=int(input())
names=[]
scores=[]
msgs=[]
for i in range(m):
    name,msg = input().strip().split(": ")
    if name not in names:
        names.append(name)
        scores.append(0)
        msgs.append([])
    msgs[names.index(name)].append(msg)
results=[]
for name in names:
    convs=msgs[names.index(name)]
    for c in convs:
        scores[names.index(name)]+=calc(c)
    results.append([name,scores[names.index(name)]])

results.sort()
for res in results:
    if res[1]>0:
        print(res[0],"happy")
    elif res[1]<0:
        print(res[0],"sad")
    else:
        print(res[0],"undefined")