from collections import defaultdict
with open('16.txt') as inputVals:
    rule,own,near=inputVals.read().split('\n\n')

rule=list(map(lambda x: str.split(x,': '),rule.splitlines()))
own=list(map(lambda x: str.split(x,','),own.splitlines()[1:],))
near=list(map(lambda x: str.split(x,','),near.splitlines()[1:]))

validTix=[]
validVals=[]
badVals=[]

for r in rule:
    ranges=r[1].split(' or ')
    ranges=list(map(lambda x: str.split(x,'-'),ranges))
    for l in ranges:
        mn=int(l[0])
        mx=int(l[1])
        validVals+=range(mn,mx+1)

validVals=set(validVals)


#Part A:
for n in near:
    isValid=True
    for v in n:
        if int(v) not in validVals:
            badVals.append(int(v))
            isValid=False
        
    if isValid:
        validTix.append(n)
    
print(f'Part A: {sum(badVals)}')

#Part B:
validTix.append(own[0])
pos=defaultdict(lambda:[])
for r in rule:
    ranges=r[1].split(' or ')
    ranges=list(map(lambda x: str.split(x,'-'),ranges))
    look=[]
    for l in ranges:
        mn=int(l[0])
        mx=int(l[1])
        look+=range(mn,mx+1)
    look=set(look)
    for l in range(len(own[0])):
        if not False in list(v in look for v in (list(int(t[l])for t in validTix))):
            pos[r[0]].append(l)
            
final={}
while len(pos)>0:
    conf=list(pos.keys())[list(map(len,pos.values())).index(1)]
    elim=pos[conf][0]
    final[conf]=pos.pop(conf)
    
    for o in pos:
        if elim in pos[o]:
            pos[o].remove(elim)

res=1
for o in final:
    if o[:9]=='departure':
        res*=int(own[0][final[o][0]])
        
print(f'Part B: {res}')