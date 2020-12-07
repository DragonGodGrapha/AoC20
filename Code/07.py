import re
with open('07.txt') as data:
    rules=data.read().splitlines()
    
    
"""rules=str.splitlines('''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.''')"""

"""rules=str.splitlines('''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.''')"""


rules=list(map(lambda x: x.split(" contain "),rules))


##PART A
x = list(r[1] for r in rules)
search=['shiny gold bag']
match=[]
while search:
    nextlevel=[]
    
    for b in search:
        for sub in x:
            #print(bool(re.findall(b,sub)))
            if re.findall(b,sub):
                nextlevel.append((rules[x.index(sub)][0])[:-1])
                match.append((rules[x.index(sub)][0])[:-1])
    search=nextlevel[:]
    
print(f'Part A: {len(set(match))}')

##PART B
y = list(r[0][:-1] for r in rules)
search=['shiny gold bag']
count=-1
while search:
    nextlevel=[]
    for b in search:
        count+=1
        for sup in y:
            if sup==b:
                content=(rules[y.index(sup)][1]).split(', ')
                content[len(content)-1]=content[len(content)-1][:-1]##Remove trailing periods
                for l in content:
                    if l[-1]=='s':l=l[:-1]
                    
                    try: num=int(l[0])
                    except: num=0
                    
                    for i in range(num):
                        nextlevel.append(l[2:])
                
                
    search=nextlevel[:]
print(f'Part B: {count}')
