


arr='389547612'


t='389125467'

cups=[int(l) for l in arr]
cups[cups.index(9)]=0
#cups+=list(range(10,1000001))
c=len(cups)
cur=cups[0]
curInd=cups.index(cur)
num=100

while num>0:
    #print(num)
    
    #print([i for i in cups])
    #print(cur)
    #print('\r')
    
    des=(cur-1)%9
    
    try: a=cups.pop((curInd+1))
    except: a=cups.pop(0)
    try: b=cups.pop((curInd+1))
    except: b=cups.pop(0)
    try: c=cups.pop((curInd+1))
    except: c=cups.pop(0)
    if des in cups:
        desInd=cups.index(des)+1
    elif (des-1)%9 in cups:
        desInd=cups.index((des-1)%9)+1
    elif (des-2)%9 in cups:
        desInd=cups.index((des-2)%9)+1
    else:
        desInd=cups.index((des-3)%9)+1
    
    cups.insert((desInd)%9,a)
    cups.insert((desInd+1)%9,b)
    cups.insert((desInd+2)%9,c)
    
    curInd=(cups.index(cur)+1)%9
    cur=cups[curInd%9]
    num-=1
    
cups[cups.index(0)]=9
st=cups.index(1)
out=''.join(map(str,cups[st+1:9]+cups[0:st]))

print(f'Part A: {out}')

