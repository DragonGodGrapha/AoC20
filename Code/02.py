with open('02.txt') as inputVals:
        data=inputVals.read().splitlines()
#data=['1-5 k: kkkkhkkkkkkkkkk','5-7 k: blkqhtxfgktdkxzkksk','15-16 x: xxxxxxxxxxxxxxlf',
#'3-5 j: fjpvj','17-20 x: zsxjrxkgxxxxxxxmxgxf']

data= [i.split(': ') for i in data]

validA=0
validB=0

for i in data:
    pw=i[1]
    rang,char=i[0].split(' ')
    mn,mx=map(int,rang.split('-'))
    
    ##Part A
    if mn<=pw.count(char)<=mx:
        validA+=1
    
    ##Part B
    if (pw[mn-1]==char)^(pw[mx-1]==char):
        validB+=1
    
        
print("Part A:",validA)
print("Part B:",validB)
