"""
lay='''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''.splitlines()
"""

with open('11.txt') as lay:
    lay=lay.read().splitlines()
    
##Boundaries
seats=[]
for line in lay:
    seats.append('o'+line+'o')
seats=['o'*len(seats[0])]+seats+['o'*len(seats[0])]

upcoming=[]
notstable=True
while notstable:
    for l in range(len(seats)):
        nextrow=''
        for s in range(len(seats[l])):
            if seats[l][s]=='o' or seats[l][s]=='.':
                nextrow+=seats[l][s]
            elif seats[l][s]=='L':
                surr=seats[l-1][s-1]+seats[l-1][s]+seats[l-1][s+1]
                surr+=seats[l][s-1]+seats[l][s+1]
                surr+=seats[l+1][s-1]+seats[l+1][s]+seats[l+1][s+1]
                if surr.count('#')==0:
                    nextrow+='#'
                else:  nextrow+='L'
                
            elif seats[l][s]=='#':
                surr=seats[l-1][s-1]+seats[l-1][s]+seats[l-1][s+1]
                surr+=seats[l][s-1]+seats[l][s+1]
                surr+=seats[l+1][s-1]+seats[l+1][s]+seats[l+1][s+1]
                if surr.count('#')>=4:
                    nextrow+='L'
                else:  nextrow+='#'
        upcoming.append(nextrow)
    
    if seats==upcoming:notstable=False
    
    seats=upcoming[:]
    upcoming=[]
    
#Part A
count=0
for r in seats:
    #print(r)
    count+=r.count('#')
print(f'Part A: {count}')

##Part B


##Boundaries
seats=[]
for line in lay:
    seats.append('o'+line+'o')
seats=['o'*len(seats[0])]+seats+['o'*len(seats[0])]

upcoming=[]
notstable=True
while notstable:
    for l in range(len(seats)):
        nextrow=''
        for s in range(len(seats[l])):
            if seats[l][s]=='o' or seats[l][s]=='.':
                nextrow+=seats[l][s]
            elif seats[l][s]=='L':
                surr=''
                for i in range(s-1,-1,-1):#Left
                    if seats[l][i]!=('.'):
                        surr+=seats[l][i]
                        break
                for i in range(s+1,len(seats[l])+1):#Right
                    if seats[l][i]!=('.'):
                        surr+=seats[l][i]
                        break
                
                for i in range(l-1,-1,-1):#Up
                    if seats[i][s]!=('.'):
                        surr+=seats[i][s]
                        break
                for i in range(l+1,len(seats)+1):#Down
                    if seats[i][s]!=('.'):
                        surr+=seats[i][s]
                        break
                for i in range(1,min(l,s)):#UL
                    if seats[l-i][s-i]!=('.'):
                        surr+=seats[l-i][s-i]
                        break
                for i in range(1,min(l,len(seats[l])-s)):#UR
                    if seats[l-i][s+i]!=('.'):
                        surr+=seats[l-i][s+i]
                        break
                for i in range(1,min(len(seats)-l,s)):#LL
                    if seats[l+i][s-i]!=('.'):
                        surr+=seats[l+i][s-i]
                        break
                for i in range(1,min(len(seats)-l,len(seats[l])-s)):#UR
                    if seats[l+i][s+i]!=('.'):
                        surr+=seats[l+i][s+i]
                        break
                
                if surr.count('#')==0:
                    nextrow+='#'
                else:  nextrow+='L'
                
            elif seats[l][s]=='#':
                surr=''
                for i in range(s-1,-1,-1):#Left
                    if seats[l][i]!=('.'):
                        surr+=seats[l][i]
                        break
                for i in range(s+1,len(seats[l])+1):#Right
                    if seats[l][i]!=('.'):
                        surr+=seats[l][i]
                        break
                
                for i in range(l-1,-1,-1):#Up
                    if seats[i][s]!=('.'):
                        surr+=seats[i][s]
                        break
                for i in range(l+1,len(seats)+1):#Down
                    if seats[i][s]!=('.'):
                        surr+=seats[i][s]
                        break
                for i in range(1,min(l,s)):#UL
                    if seats[l-i][s-i]!=('.'):
                        surr+=seats[l-i][s-i]
                        break
                for i in range(1,min(l,len(seats[l])-s)):#UR
                    if seats[l-i][s+i]!=('.'):
                        surr+=seats[l-i][s+i]
                        break
                for i in range(1,min(len(seats)-l,s)):#LL
                    if seats[l+i][s-i]!=('.'):
                        surr+=seats[l+i][s-i]
                        break
                for i in range(1,min(len(seats)-l,len(seats[l])-s)):#UR
                    if seats[l+i][s+i]!=('.'):
                        surr+=seats[l+i][s+i]
                        break
                
                
                if surr.count('#')>=5:
                    nextrow+='L'
                else:  nextrow+='#'
        upcoming.append(nextrow)
    
    if seats==upcoming:
        notstable=False
    seats=upcoming[:]
    #for r in seats:
    #    print(r)
    #print('\n\n')
    upcoming=[]
    
count=0
for r in seats:
    #print(r)
    count+=r.count('#')
print(f'Part B: {count}')
