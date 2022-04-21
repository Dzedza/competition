def value(card):
    if card[0] in ['2','3','4','5','6','7','8','9']:
        return int(card[0])
    else:
        return 10



t=int(input())

for i in range(t):
    deck=input().split()
    y=0
    first25= deck[27:52]
    rest=deck[0:27]
    for j in range(3):
        x=value(rest[-1])
        y+=x
        rest=rest[0:len(rest)-1-(10-x)]
    deck=rest+first25
    print("Case "+str(i+1)+": "+str(deck[y-1]))


