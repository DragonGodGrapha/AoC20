def transform(k,t,**kwargs):
    
    if 'mode' in kwargs and kwargs['mode']=='search':
        v=1
        ct=0
        while v!=t:
            v=(v*k)%20201227
            ct+=1
        return ct
    
    else:
        v=1
        for _ in range(t):
            v=(v*k)%20201227
        return v

with open('25.txt') as vals:
    p1,p2=map(int,vals.read().splitlines())

l1=transform(7,p1,mode='search')
l2=transform(7,p2,mode='search')

e1=transform(p1,l2)
e2=transform(p2,l1)
if e1==e2:
    print(f'Part A: {e1}')