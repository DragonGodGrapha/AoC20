import re


'''data=''''''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''

with open('04.txt') as data:
    data=list(map(lambda x: re.split(" |\n",x),data.read().split('\n\n')))

data[len(data)-1].pop()
req=['byr','iyr','eyr','hgt','hcl','ecl','pid']
valid=0

passed=[]
##A
for i in data:
    fields=[]
    for j in i:
        fields.append(j[:3])
    var=list(set(fields)^set(req))
    if var==[] or var==['cid']:
        valid+=1
        passed.append(i)
print(f'Part A: {valid}')


##B
validB=0
for i in passed:
    goodfield=0
    for j in i:
        field=j[:3]
        val=j[4:]
        if field in['byr','iyr','eyr']:
            if val.isdigit() and len(val)==4:
                if field=='byr' and 1920<=int(val)<=2002:
                    pass
                elif field=='iyr' and 2010<=int(val)<=2020:
                    pass
                elif field=='eyr' and 2020<=int(val)<=2030:
                    pass
                else:continue               
            else:continue
            
        elif field=='pid':
            if not (val.isdigit() and len(val)==9):
                continue
        
        elif field=='ecl':
            if val not in ['amb','blu','brn','gry','grn','hzl','oth']:
                continue
        
        elif field=='hgt':
            if val[-2:]=='in' and 59<=int(val[:-2])<=76:
                pass
            elif val[-2:]=='cm' and 150<=int(val[:-2])<=193:
                pass                
            else: continue
        
        elif field=='hcl':
            if val[0]!='#':continue
            elif bool(re.match('([0-9]|[a-m]){6}',val[1:]) and not re.match('([0-9]|[a-m]){7}',val[1:])):
                pass
            else:continue
        goodfield+=1
        if goodfield==len(i):validB+=1
        
print(f'Part B: {validB}')

        
    