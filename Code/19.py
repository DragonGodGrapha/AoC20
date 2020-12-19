from collections import defaultdict

def ruleMaker(raw):
    rules=defaultdict(lambda:'')
    for rule in raw:
        k,v=rule.split(': ')
        if v[0]=='"':
            rules[int(k)]=v[1:-1]
        else:
            v=v.split(' | ')
            t=[]
            for r in v:
                t.append([int(s) for s in r.split()])
            rules[int(k)]=t
    return rules

def match(inp,rule):
    if len(rule)>len(inp):
        return False
    elif len(rule)==0 or len(inp)==0:
        return (len(rule)==0 and len(inp)==0)
    r=rule.pop()
    if isinstance(r,str):
        if inp[0]==r:
            return match(inp[1:],rule.copy())
    else:
        for j in rules[r]:
            if match(inp,rule + list(reversed(j))):
                return True
    return False
    
def count(rules, inp):
    total = 0
    for i in inp:
        if match(i, list(reversed(rules[0][0]))):
            total += 1
    return total


with open('19.txt') as inputVals:
    rules,inp=inputVals.read().split('\n\n')
rules=rules.splitlines()
inp=inp.splitlines()
rules=ruleMaker(rules)
print(f'Part A: {count(rules,inp)}')
rules[8]=[[42],[42,8]]
rules[11]=[[42,31],[42,11,31]]
print(f'Part B: {count(rules,inp)}')


