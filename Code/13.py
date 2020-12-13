from math import prod
import sympy.ntheory.modular

with open('13.txt') as data:
    time,sch=data.read().splitlines()
"""
time,sch='''939
7,13,x,x,59,x,31,19'''.splitlines()"""
sch=list(map(int,map(lambda x: x.replace('x','1'),sch.split(','))))

time=int(time)
departs=[]
for i in sch:
    if i==1:
        continue
    delta=(i*((time//i)+1))-time
    departs.append([i,delta])
print(f'Part A: {prod(min(departs,key=lambda x:x[1]))}')


m,r = zip(*((b,b-i) for i,b in enumerate(sch) if b>1))
print(f'Part B: {sympy.ntheory.modular.crt(m,r)[0]}')