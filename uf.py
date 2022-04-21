n=int(input())

vertices=[i for i in range(n)]

def find(i):
    j = vertices[i]
    k = i
    while i!=j:
        i=j
        j=vertices[j]
    while k!=i:
        tmp=vertices[k]
        vertices[k]=i
        k=tmp
    return i
def unite(i,j):
    vertices[find(i)]=vertices[find(j)]
    p=find(i)