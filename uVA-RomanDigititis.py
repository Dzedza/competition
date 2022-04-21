def intToRoman(n):
    nums = [100,90,50,40,10,9,5,4,1]
    sym = ["c","xc","l","xl","x","ix","v","iv","i"]
    romanNum = ''
    i = 0
    while n>0:
        for _ in range(n // nums[i]):
            romanNum += sym[i]
            n -= nums[i]
        i += 1
    return romanNum

n=int(input())
while n!=0:
    count={"i":0,"v":0,"x":0,"l":0,"c":0}
    for j in range(1,n+1):
        v=intToRoman(j)
        for c in v:
            count[c]+=1
    print(str(n)+": "+str(count["i"])+" i, "+str(count["v"])+" v, "+
    str(count["x"])+" x, "+str(count["l"])+" l, "+str(count["c"])+" c")
    n=int(input())
