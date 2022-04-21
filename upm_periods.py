import sys
from fractions import Fraction

for n in sys.stdin.readlines():
    n=n.strip().lstrip("0")
    if n=="":
        print(0)
        continue
    if "." not in n:
        print(n)
        continue
    if "(" in n:
        place=n.index("(")
        if int(n[place+1:len(n)-1])==0:
            n=n[:place]
    if ".(" in n:
        if n[0]!=".":
            dotp=n.index(".")
            begin=int(n[:dotp])
        else:
            begin=0
        repet=n[place+1:len(n)-1]
        x,y=int(repet),10**len(repet)-1
        fr=Fraction(x,y)
        a,b=fr.numerator,fr.denominator
        a+=begin*b
        fr=Fraction(a,b)
        a,b=fr.numerator,fr.denominator
        if b==1:
            print(a)
        else:
            print(str(a)+"/"+str(b))
        continue
    if "(" not in n:
        dot=n.index(".")
        power=10**len(n[dot:len(n)])
        m=n[:dot]+n[dot+1:]
        a,b=Fraction(int(m),power).numerator,Fraction(int(m),power).denominator
        if b==1:
            print(a)
        else:
            print(str(a)+"/"+str(b))
        continue
    s=n[:place]
    dot=n.index(".")
    power=10**len(s[dot:len(s)])
    beforeRep=len(s[dot+1:len(s)])
    rep=n[place+1:len(n)-1]
    denom=10**len(rep)-1
    numer2=int(n[place+1:len(n)-1])
    denom2=denom
    denom1=power
    if "0" in rep:
        denom1=denom1//10
    numer1=int(n[:place].replace(".",""))
    finalD=denom1*denom2
    numerF=numer1*denom2+numer2
    res=Fraction(numerF,finalD)
    a,b=res.numerator,res.denominator
    if b==1:
        print(a)
    else:
        print(str(a)+"/"+str(b))
