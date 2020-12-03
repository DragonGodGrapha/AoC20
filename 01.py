from itertools import combinations as comb
import math

#data=[1721,979,366,299,675,1456]

with open('01.txt') as inputVals:
        data=list(map(int,inputVals.read().splitlines()))

##Part 1
pairs=list(comb(data,2))
for i in pairs:
    if sum(i)==2020:
        print("Pairs: ",math.prod(i))
        break


##Part 2
sets=list(comb(data,3))
for j in sets:
    if sum(j)==2020:
        print("Triples: ",math.prod(j))
        break