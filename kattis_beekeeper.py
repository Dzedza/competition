n=int(input())
while n!=0:
    words=[]
    for i in range(n):
        words.append(input().strip())   
    m=-1
    res=""
    for word in words:
        cnt=0
        for i in range(1,len(word)):
            if word[i] in ['a','e','i','o','u','y'] and word[i]==word[i-1]:
                cnt+=1
        if cnt>m:
            m=cnt
            res=word
    print(res)
    n=int(input())