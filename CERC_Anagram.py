import sys
 
n = int(sys.stdin.readline().strip())
s = set()
 
for i in range(n):
    k = len(s)
    w = sys.stdin.readline().strip()
    word = ''.join(sorted(w))
    s.add(word)
    if len(s)-k == 1:
        print(w)
