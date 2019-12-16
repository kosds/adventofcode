import math

oldtest = ['3,9,8,9,10,9,4,9,99,-1,8',
         '3,9,7,9,10,9,4,9,99,-1,8',
         '3,3,1108,-1,8,3,4,3,99',
         '3,3,1107,-1,8,3,4,3,99',
           '3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9',
         '3,3,1105,-1,9,1101,0,0,12,4,12,99,1']

tests = [
'''.#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....#...###..
..#.#.....#....##''',
'''.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##'''
    ]


def gcded (aa, bb):
##    print(aa, bb)
    a, b = abs(aa), abs(bb)
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    gcd = a + b
##    print(aa, bb, gcd)
    if gcd == 0:
        return aa, bb
    else:
        return  aa // gcd, bb // gcd    

def proc(grid):
    asters = []
    for i, line in enumerate(grid.split('\n')):
        for j, aster in enumerate(line):
            if aster == '#':
                asters.append((i,j))
##    print(asters)
    visions = {}
    for asterbase in asters:
        vision = dict()
        for aster in asters:
            a, b = aster[0] - asterbase[0], aster[1] - asterbase[1]
            res = gcded(a,b)
            if res in vision:
                vision[res].append(aster)
            else:
                vision[res] = [aster]
        visions[asterbase] = (len(vision) - 1, vision)
##    print(visions)
    maxx = max(visions.items(), key=lambda a: a[1][0])
##    print(max(visions.items(), key=lambda a: a[1][0]))
    vision = maxx[1][1]
##    print(vision)
    pos = maxx[0]
    vision.pop((0,0))
    visionangle = {}
    for el in vision:
##        if el[1] == 0:
####            print(el, math.atan(math.inf * el[0]))
##            visionangle[el] = math.atan2(math.inf * el[0]) 
##        else:
####            print(el, math.atan(el[0]/el[1]))
        visionangle[el] = math.atan2(el[1], el[0])
##        print(el, math.atan2(-el[1], el[0]))
    vision = {a: (visionangle[a],
                  [(el, abs(abs(el[0]) - abs(pos[0])) +
                     abs(abs(el[1]) - abs(pos[1])))
                   for el in vision[a]])
              for a in vision}
##    print(vision)
    vision = list(vision.items())
    for el in vision:
        el[1][1].sort(key=lambda a: a[1], reverse = True)
    vision.sort(key = lambda a: a[1][0], reverse = True)
##    for a in vision:
##        print(a)
    print()
    count = 0
    go = True
    while go:
        go = False
        for el in vision:
            if el[1][1]:
                poped = el[1][1].pop()        
                count += 1
##                print(count, poped)
                if count == 200:
                    print(poped)
                go = True
##    return max(visions.values())
    
    
def main():
    for test in tests:
        res = proc(test)
        print('output =', res)
        print()
    with open('input10.txt') as f:
        res = proc(f.read())
        print('output =', res)
        print()
if __name__ == '__main__':
    main()
