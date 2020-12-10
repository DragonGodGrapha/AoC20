"""
vals='''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''.splitlines()
vals=list(map(int,vals))"""



with open('10.txt') as vals:
    vals=list(map(int,vals.read().splitlines()))


vals.append(0)
vals.append(max(vals)+3)
vals.sort()
ones=0
twos=0
threes=0
for i in range(len(vals)-1):
    delta=vals[i+1]-vals[i]
    if delta==1:ones+=1
    elif delta==2:twos+=1
    elif delta==3:threes+=1
print(f'Part A: {ones*threes}')



##Part B
lindict={0:1}
for val in vals[1:]:
    lindict[val]=0
    if val-1 in lindict:
        lindict[val]+=lindict[val-1]
    if val-2 in lindict:
        lindict[val]+=lindict[val-2]
    if val-3 in lindict:
        lindict[val]+=lindict[val-3]

print(f'Part B: {lindict[vals[-1]]}')

        