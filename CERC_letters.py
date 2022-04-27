import sys
 
n,m,k = map(int, sys.stdin.readline().strip().split())
moves = sys.stdin.readline().strip()
l = [sys.stdin.readline().strip() for i in range(n)]
 
def transpose(mat):
    cols=[]
    for i in range(len(mat[0])):
        s=''
        for j in range(len(mat)):
            s=s+mat[j][i]        
        cols.append(s)
    return cols
 
 
def gravity(c,letters):
    l1=[]
    if c == 'R':
        for i in range(len(letters)):
            cnt = letters[i].count('.')
            l1.append('.'*cnt+letters[i].replace('.',''))
    elif c=='L':
        for i in range(len(letters)):
            cnt = letters[i].count('.')
            l1.append(letters[i].replace('.','')+'.'*cnt)
    else:
        l1=transpose(letters)
        if c== 'U':
            l1=transpose(gravity('L',l1))
        if c== 'D':
            l1=transpose(gravity('R',l1))
    return l1
 
for i in range(k):
    l=gravity(moves[i],l)
 
for i in range(n):
    print(l[i])
