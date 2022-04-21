n= int(input())
for i in range(n):
    print(i)
    ans= input()
    if ans=="Bingo!":
        quit()
for i in range(n-1,-1,-1):
    print(i)
    ans= input()
    if ans=="Bingo!":
        quit()