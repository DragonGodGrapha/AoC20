from math import prod
def allEdges(tile):
    info=tile[1:]
    edges=[]
    edges.append(info[0])
    edges.append(info[0][::-1])
    edges.append(info[len(info)-1])
    edges.append(info[len(info)-1][::-1])
    edges.append(''.join(info[r][0] for r in range(len(info))))
    edges.append(''.join(info[r][0] for r in reversed(range(len(info)))))
    edges.append(''.join(info[r][len(info[0])-1] for r in range(len(info))))
    edges.append(''.join(info[r][len(info[0])-1] for r in reversed(range(len(info)))))
    return edges
"""
t='''Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...'''.split('\n\n')
"""
with open('20.txt') as t:
    t=t.read().split('\n\n')

t=list(map(lambda x:x.splitlines(),t))[:-1]
edges=[]
pieces={}
pieceborder={}

for p in t:
    edge=allEdges(p)
    edges+=edge
    pieces[p[0][-5:-1]]=edge

for p in pieces:
    count=0
    check=edges[:]
    for j in pieces[p]:
        check.remove(j)
    for j in pieces[p]:
        if j in check:
            count+=1
        pieceborder[p]=count
corners=[]
for q in pieceborder.items():
    if q[1]==4:
        corners.append(int(q[0]))

print(f'Part A: {prod(corners)}')
"""Part B could not be completed"""


