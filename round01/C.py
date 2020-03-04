from math import pi, ceil

xa, ya, xc, yc = map(int, input().split())
dist = ((xa-xc)**2+(ya-yc)**2)**(1/2)
print(round(dist, 4))