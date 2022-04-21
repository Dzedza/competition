open= ["(","[","{","<"]

def check(word):
    stack= []
    for c in word:
        if c in open:
            stack.append(c)
        else:
            if stack==[]:
                return False
            cmp= stack.pop()
            if cmp=="(" and c!=")":
                return False
            if cmp=="[" and c!="]":
                return False
            if cmp=="{" and c!="}":
                return False
            if cmp=="<" and c!=">":
                return False
    if stack==[]:
        return True
    return False


s= input()
dp= [[-1 for i in range(len(s))] for i in range(len(s))]
q= int(input())
res=""
for a in range(q):
    z,k= map(int,input().split())
    for i in range(z,k):
        for j in range(z,k):
            if not dp[i][j] and s[j-1] in closed:
                res+="0"
                break
    if check(s[z-1:k]):
        res+="1"
    else:
        res+="0"
print(res)