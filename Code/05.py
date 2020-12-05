with open('05.txt') as inputVals:
        bps=inputVals.read().splitlines()

ids=[]
for n in bps:
    n=n.replace('F','0')
    n=n.replace('B','1')
    n=n.replace('L','0')
    n=n.replace('R','1')
    row=int(n[:7],2)
    col=int(n[7:],2)
    seatID=8*row+col
    ids.append(seatID)
#Part A
print(max(ids))

for i in range(1,max(ids)):
    if (i+1 in ids) and (i-1) in ids and (not i in ids):
        print(f"Seat {i} missing")