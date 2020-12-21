from collections import defaultdict


label='''mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)'''.splitlines()

with open('21.txt') as label:
    label=label.read().splitlines()


label=list(map(lambda x: x.split(' (contains '), label))

ingr=list(map(lambda x: x[0].split(),label))
allr=list(map(lambda x: x[1][:-1].split(', '),label))


alllist=list(set().union(*allr))
ingrlist=list(set().union(*ingr))
flatingr=[i for r in ingr for i in r]

alldict=defaultdict(lambda x:[])
for i in alllist:
    ol=[]
    for j,aller in enumerate(allr):
        if i in aller:
            ol.append(ingr[j])
    alldict[i]=list(set.intersection(*map(set,ol)))
    
for k in alldict.values():
    for j in k:
        while j in flatingr:
            flatingr.remove(j)
            
print(f'Part A: {len(flatingr)}')

finaldict={}
while len(alldict)>0:
    conf=list(alldict.keys())[list(map(len,alldict.values())).index(1)]
    finaldict[conf]=alldict[conf][0]
    r = alldict.pop(conf)[0]
    for o in alldict:
        if r in alldict[o]:
            alldict[o].remove(r)
order=sorted(list(finaldict.keys()))
d=''
for r in order:
    d+=finaldict[r]+','
d=d[:-1]
print(f'Part B: {d}')
