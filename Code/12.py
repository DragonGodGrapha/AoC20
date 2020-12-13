from math import sin,cos,radians as rad
"""
inst='''F10
N3
F7
R90
F11'''.splitlines()
"""

with open('12.txt') as inst:
    inst=inst.read().splitlines()
facing=0
px=0#cos
pz=0#sin
##Part A
for i in inst:
    c=i[:1]
    v=int(i[1:])
    if c=='N':pz+=v
    elif c=='S':pz-=v
    elif c=='E':px+=v
    elif c=='W':px-=v
    elif c=='L':facing=(facing+v)%360
    elif c=='R':facing=(facing-v)%360
    elif c=='F':
        px+=(v*round(cos(rad(facing))))
        pz+=(v*round(sin(rad(facing))))
print(f'Part A: {abs(px)+abs(pz)}')

##Part B
px=0
pz=0
wx=10
wz=1
for i in inst:
    c=i[:1]
    v=int(i[1:])
    if c=='F':
        px+=v*wx
        pz+=v*wz
    elif c=='N':wz+=v
    elif c=='S':wz-=v
    elif c=='E':wx+=v
    elif c=='W':wx-=v
    elif c=='L':
        for a in range(v//90):
            wx,wz=-wz,wx
    elif c=='R':
        for a in range(v//90):
            wx,wz=wz,-wx
print(f'Part B: {abs(px)+abs(pz)}')