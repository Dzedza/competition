import sys
import math
 
tx, ty, sx, sy = [int(x) for x in sys.stdin.readline().split()]
 
def get_line(x, y, a, b):
    return [b, -a, a*y - b*x]
 
a, b, c = get_line(tx, ty, sx, sy)
sqrt = math.sqrt(a**2 + b**2)
 
def distance(p):
    k = p[0] 
    c1, c2 = p[1], p[2]
    v1, v2 = p[3], p[4]
    center_distance = (a*c1 + b*c2 + c) / sqrt 
    if center_distance == 0:
        return 0
    p, q = sx, sy
    alpha = math.atan2(v2, v1)
    if center_distance < 0:
        p, q = q, -p
    else:  # center_distance >= 0:
        p, q = -q, p
    beta = math.atan2(q, p)
    l = (beta - alpha) * k // (2*math.pi)
    angle1 = 2 * math.pi / k * l
    angle2 = 2 * math.pi / k * (l+1)
    x1, y1 = v1 * math.cos(angle1) - v2 * math.sin(angle1) , v1 * math.sin(angle1) + v2 * math.cos(angle1)
    x2, y2 = v1 * math.cos(angle2) - v2 * math.sin(angle2) , v1 * math.sin(angle2) + v2 * math.cos(angle2)
    d1 = (a*(c1+x1) + b*(c2+y1) + c) / sqrt 
    d2 = (a*(c1+x2) + b*(c2+y2) + c) / sqrt 
    if d1 < 0 and center_distance > 0 or d1 > 0 and center_distance < 0:
        return 0
    if d2 < 0 and center_distance > 0 or d2 > 0 and center_distance < 0:
        return 0
 
    if abs(d1) < abs(d2):
        least = d1
    else:
        least = d2  
    return abs(least)
 
 
n = int(sys.stdin.readline())
for i in range(n):
    print(distance([int(x) for x in sys.stdin.readline().split()]))
