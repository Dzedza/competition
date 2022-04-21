def piglatin(s):
    if s[0] in ["a","e","i","o","u","y"]:
        return s+"yay"
    for i in range(len(s)):
        if s[i] in ["a","e","i","o","u","y"]:
            break
    return s[i:]+s[:i]+"ay"

contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

for line in contents:
    res=""
    line=line.split()
    for i in range(len(line)-1):
        res=res+piglatin(line[i])+" "
    res=res+piglatin(line[-1])
    print(res)

