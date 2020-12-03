import math
"""
form=['..##.......',
      '#...#...#..',
      '.#....#..#.',
      '..#.#...#.#',
      '.#...##..#.',
      '..#.##.....',
      '.#.#.#....#',
      '.#........#',
      '#.##...#...',
      '#...##....#',
      '.#..#...#.#']
"""

with open('03.txt') as inputVals:
        form=inputVals.read().splitlines()


posX=0
posZ=0
cycle=len(form[1])


##Part A
dx=3
dz=1
count=0
while posZ+dz<=len(form)-1:
    posX=(posX+dx)%cycle
    posZ+=dz
    if form[posZ][posX]=='#':
        count+=1
        
print(f"Part A: {count}")


##Part B
counts=[]
slopes=[[1,1],[3,1],[5,1],[7,1],[1,2]]

for x,z in slopes:
    temp=0
    posX=0
    posZ=0
    
    while posZ+z<=len(form)-1:
        posX=(posX+x)%cycle
        posZ+=z
        if form[posZ][posX]=='#':
            temp+=1
    counts.append(temp)
    
print(f"Part B: {math.prod(counts)}")   