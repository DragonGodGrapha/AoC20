#rule=[0,3,6]
rule=[9,12,1,4,17,0,18]

lim=30000000

pos={}
for seq,p in enumerate(rule):
    pos[p]=[seq]
    
last=rule[-1]

for i in range(len(rule),lim):
    if i%1000==0:print(i)
    count=len(pos[last])
    if count>1:
        last=pos[last][-1]-pos[last][-2]
        if last in pos:
            pos[last].append(i)
        else: pos[last]=[i]
        
    else:
        last=0
        pos[last].append(i)
    if i==2019:r20=last
   
print(f'Part A: {r20}')
print(f'Part B: {last}')