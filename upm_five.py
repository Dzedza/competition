n=int(input())
moves=[(0,1),(1,1),(1,0),(1,-1)]
play=[set(),set()]
players=["Linus","Snoopy"]
        

def check(p,x,y):
    for a,b in moves:
        count= 0
        for j in range(-4,5):
            if (x+a*j,y+b*j) in play[p]:
                count+=1
                if count==5:
                    return True
            else:
                count= 0
    return False

i=1
won=False
while not won and i<n+1:
    if i%2==1:
        player=1
        num=i//2+1
    else:
        player=0
        num=i//2
    xx,yy= map(int,input().split())
    play[player].add((xx,yy))
    if check(player,xx,yy):
        print(players[player],num)
        won=True
    i+=1

if not won:
    print("neodloceno")

    


