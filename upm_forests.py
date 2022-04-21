import sys
sys.setrecursionlimit(2500000)

def check_valid(a,b,label):
    if a<n and b<m and a>=0 and b>=0 and visited[a][b]==0 and image[a][b]==label:
        return True
    return False

moves=[(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
def find_connected(x,y,color):
    visited[x][y]=1
    for move in moves:
        a,b=x+move[0],y+move[1]
        if check_valid(a,b,image[x][y]):
            find_connected(a,b,color)

n,m= map(int,input().split())
while (n,m)!=(0,0):
    visited=[[0 for i in range(m)] for j in range(n)]
    image=[[c for c in input()]for i in range(n)]
    count=0
    for i in range(n):
        for j in range(m):
            if visited[i][j]==0:
                count+=1
                find_connected(i,j,image[i][j])
    print(count)
    n,m= map(int,input().split())