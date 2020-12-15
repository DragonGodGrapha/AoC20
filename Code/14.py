from itertools import product

def apply(mask,val):
    out=''
    for j in range(len(mask)):
        if mask[j]!='X':
            out+=mask[j]
        else:
            out+=val[j]
    return out

def applyV2(mask,pos):
    out=''
    for j in range(len(mask)):
        if mask[j]!='0':
            out+=mask[j]
        else:
            out+=pos[j]
    return out

def dequantum(num):
    options={'X':['0','1']}
    combos = [(c,) if c not in options else options[c] for c in num]
    return (''.join(o) for o in product(*combos))

with open('14.txt') as inst:
    inst=list(filter(bool,map(str.splitlines,inst.read().split("mask = "))))



test='''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0'''
test2='''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''

mem1={}
mem2={}

test=list(filter(bool,map(str.splitlines,test.split("mask = "))))
test2=list(filter(bool,map(str.splitlines,test2.split("mask = "))))

for j in inst:
    mask=j[0]
    for c in j[1:]:
        r=c.split('] = ')
        address=int(r[0][4:])
        val=(bin(int(r[1]))[2:]).zfill(len(mask))
        mv=int(apply(mask,val),base=2)
        mem1[address]=mv
        
        pos=(bin(int(address))[2:]).zfill(len(mask))
        val2=int(r[1])
        for i in list(map(lambda x:int(x,base=2),list(dequantum(applyV2(mask,pos))))):
            mem2[i]=val2
            
        
print(f'Part A: {sum(mem1.values())}')
print(f'Part B: {sum(mem2.values())}')       
        