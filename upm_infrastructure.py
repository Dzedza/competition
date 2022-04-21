import sys

roads=[]
for line in sys.stdin.readlines():
    roads.append(line.strip().split())

cities=[]
for road in roads:
    for c in road:
        if c not in cities:
            cities.append(c)
vertices=[i for i in range(len(cities))]

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
    p=find(i)
    q=find(j)
    vertices[p]=vertices[q]
    for k in range(len(vertices)):
        if vertices[k]==p:
            vertices[k]=q


for road in roads:
    unite(cities.index(road[0]),cities.index(road[1]))
vertices=list(set(vertices))
res=[]
for v in range(1,len(vertices)):
    print(cities[vertices[v-1]],cities[vertices[v]])

