

accumulator=0

"""
inst='''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''
inst=list(map(lambda x: x.split(" "),inst.splitlines()))"""

with open('08.txt') as inst:
    inst=list(map(lambda x: x.split(" "),inst.read().splitlines()))

hasRun=[]

index=0
while index<=len(inst)-1:
    if index in hasRun:
        print(f"Loop found: index {index}")
        break
    
    hasRun.append(index)
    command=inst[index][0]
    val=inst[index][1]
    if command=='nop':
        index+=1
    
    elif command=='acc':
        if val[0]=='-':accumulator-=int(val[1:])
        else: accumulator+=int(val[1:])
        index+=1
    elif command=='jmp':
        if val[0]=='-':index-=int(val[1:])
        else: index+=int(val[1:])

#Part A
print(f'Accumulator value: {accumulator}')
    
##Part B
for j in list(reversed(hasRun[:])):
    if inst[j][0]=='jmp':
        inst[j][0]='nop'
    elif inst[j][0]=='nop':
        inst[j][0]='jmp'
    else:continue
    print(j)
    looped=False
    accumulator=0
    hasRun=[]
    index=0
    while index<=len(inst)-1:
        if index in hasRun:
            #print(f"Loop found: index {index}")
            looped=True
            break
        
        hasRun.append(index)
        command=inst[index][0]
        val=inst[index][1]
        if command=='nop':
            index+=1
        
        elif command=='acc':
            if val[0]=='-':accumulator-=int(val[1:])
            else: accumulator+=int(val[1:])
            index+=1
        elif command=='jmp':
            if val[0]=='-':index-=int(val[1:])
            else: index+=int(val[1:])
    #Part B
    if not looped:
        print(f'Changed Command at {j}, no loop found')
        print(f'Accumulator value: {accumulator}')
        break
    
