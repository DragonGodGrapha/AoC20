import re
from collections import defaultdict as ddict

with open('24.txt') as lines:
    lines=lines.read().splitlines()

"""lines='''sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew'''.splitlines()"""
    

tiles=ddict(lambda:False)

for tile in lines:
    loc=re.findall("e|se|sw|w|nw|ne",tile)
    v=loc.count("ne") + loc.count("nw")-loc.count("se")-loc.count("sw")
    h = loc.count("e")-loc.count("w")-loc.count("nw")+loc.count("se")
    tiles[((v,h))]=not tiles[(v,h)]

print(f'Part A: {sum(list(tiles.values()))}')

floor=tiles
for i in range(100):
    nextfloor = ddict(lambda: False)
    
    for pos,v in floor.items():
        
        for s in [(0, -1), (1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0)]:
            t=(pos[0]+s[0],pos[1]+s[1])
            if t not in nextfloor:
                nextfloor[t]=floor.get(t,False)
                
    for pos,v in nextfloor.items():
        sur=sum([floor[(pos[0]+s[0],pos[1]+s[1])] for s in [(0, -1), (1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0)]])
        
        if v and (sur==0 or sur>2):nextfloor[pos]=False
        elif sur==2: nextfloor[pos]=True
    floor=nextfloor
    #print(f'Day {i+1}: {sum(list(floor.values()))}')
print(f'Part B: {sum(list(floor.values()))}')