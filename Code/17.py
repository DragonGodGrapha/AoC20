from collections import deque
from itertools import product

def column(lst,ind):
    return list(r[ind] for r in lst)

def expand(lst):
    exp=lst.copy()
    size=len(exp[0][0])
    nextSize=size
    for l in exp:
        if ('#' in l[0]) or ('#' in l[-1]) or ('#' in column(l,0)) or ('#' in column(l,-1)):
            nextSize=size+2
    
    emptyrow='.'*nextSize
    
    if nextSize!=size:
        for l in exp:
            for p,r in enumerate(l):
                r='.'+r+'.'
                l[p]=r
            l.appendleft(emptyrow)
            l.append(emptyrow)
    emptylayer=deque([])
    for l in range(nextSize):
        emptylayer.append(emptyrow)  
    
    for r in exp[0]:
        if '#' in r:
            exp.appendleft(emptylayer)
            break
    for r in exp[-1]:
        if '#' in r:
            exp.append(emptylayer)
            break
    return exp
        
        

"""test=deque('''.#.
..#
###'''.splitlines())"""
with open('17.txt') as test:
    test=deque(test.read().splitlines())

test=deque([test])
test=expand(test)
sur=list(product([-1,0,1],repeat=4))
sur.remove((0,0,0))

for j in range(6):
    test=expand(test)
    nextcube=deque([])
    
    for z,layer in enumerate(test):
        nextlayer=deque([])
        for y,row in enumerate(test[z]):
            nextrow=''
            for x,cell in enumerate(test[z][y]):
                surr=0
                for dx,dy,dz in sur:
                    if (0<=x+dx<len(row)) and (0<=y+dy<len(row)) and (0<=z+dz<len(test)):
                        if test[z+dz][y+dy][x+dx]=='#':
                                surr+=1
                    
                
                if (surr<2 or surr>3) and cell=='#':
                    nextcell='.'
                elif surr==3 and cell=='.':
                    nextcell='#'
                else:
                    nextcell=cell
                nextrow+=nextcell
            nextlayer.append(nextrow)    
        nextcube.append(nextlayer)
        #print(nextlayer)
    test=nextcube.copy()
    test=expand(test)
    #print(f'Cycle {j}')
    """for c,r in enumerate(test):
        print('\n')
        
        for l in r:
            print(l)"""
        
        
        
    
count=0
for s in test:
    for r in s:
        count+=r.count('#')
            

