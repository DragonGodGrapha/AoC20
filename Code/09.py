from itertools import combinations as co
"""
code='''35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''.splitlines()
code=list(map(int,code))
"""

with open('09.txt') as code:
    code=list(map(int,code.read().splitlines()))



pre=25
for j in range(pre,len(code)):
    val=code[j]
    valid=list(map(sum,co(code[j-pre:j],2)))
    if val not in valid:
        print(f'Invalid value: {val} at {j}')
        check=val

for k in range(len(code)):
    for m in range(k+1,len(code)):
        tot=sum(code[k:m+1])
        if tot==check:
            w=max(code[k:m+1])+min(code[k:m+1])
print(f'Part B: {w}')

