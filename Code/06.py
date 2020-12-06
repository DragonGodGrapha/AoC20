   

with open('06.txt') as data:
    data=list(map(lambda x: x.split("\n"),data.read()[:-1].split('\n\n')))
    
groupsums=[]
groupprods=[]
for j in data:
    letters=set(''.join(j))
    groupsums.append(len(letters))
    
    groupprods.append(len(set.intersection(*map(set,j))))
    

#Part A
print(f'Part A: {sum(groupsums)}')

#Part B
print(f'Part B: {sum(groupprods)}')
