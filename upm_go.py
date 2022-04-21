from sys import stdin

lines=[i.strip().split() for i in stdin.readlines()]
moves=[(int(p[0]),int(p[1])) for p in lines]

board=[["." for j in range(19)] for i in range(19)]
groups={"B":[],"W":[]}

def opposite(s):
    if s=="B":
        return "W"
    return "B"

def checkGroups(y,x,p):
    res=[]
    for i in range(len(groups[p])):
        for place in groups[p][i]:
            b,a=place
            if (a-1==x and b==y) or (a==x and b-1==y) or (a+1==x and b==y) or (a==x and b+1==y):
                if i not in res:
                    res.append(i)
    if possibleGroups==[]:
        groups[play].append([(c,r)])
    gr=[]
    for num in res:
        gr+=groups[play][num]
    groups[play]=[groups[play][n] for n in range(len(groups[play])) if n not in res]
    groups[play].append[gr]


player=0
for move in moves:
    if player%2==0:
        play="B"
    else:
        play="W"
    c,r= move
    c-=1
    r-=1
    if board[r][c]!=".":
        continue
    possibleGroups=checkGroups(c,r,play)
    
        
        