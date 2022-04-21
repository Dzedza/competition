def getScore(l,s):
    if l[s]=="/":
        if l[s+1] in ["/","X"]:
            return 20 - int(l[s-1])
        return 10+getScore(l,s+1)- int(l[s-1])
    elif l[s]=="X":
        if l[s+1] in ["/","X"] and l[s+2] in ["/","X"]:
            return 30
        if l[s+1] in ["/","X"] and l[s+2] not in ["/","X"]:
            return 20+getScore(l,s+2)
        if l[s+1] not in ["/","X"] and l[s+2] in ["/","X"]:
            return 20+getScore(l,s+1)
        return 10+getScore(l,s+1)+getScore(l,s+2)
    else:
        return int(l[s])

inp = input()
while inp != "Game Over":
    scores = inp.split()
    final = 0
    for i in range(len(scores)):
        print(scores[i],getScore(scores,i))
        final+=getScore(scores,i)
        if i==len(scores)-3 and scores[i] in ["/","X"]:
            break
    print(final)
    inp=input()