import itertools

oldtest = ['3,9,8,9,10,9,4,9,99,-1,8',
         '3,9,7,9,10,9,4,9,99,-1,8',
         '3,3,1108,-1,8,3,4,3,99',
         '3,3,1107,-1,8,3,4,3,99',
           '3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9',
         '3,3,1105,-1,9,1101,0,0,12,4,12,99,1']

tests = [
'''.#..#
.....
#####
....#
...##'''
    ]

testss = [
(89,89),
(3,4),
(12,-12),
(-6,24)
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
        vision = set()
        for aster in asters:
            a, b = aster[0] - asterbase[0], aster[1] - asterbase[1]
            vision.add(gcded(a,b))
        visions[asterbase] = len(vision) - 1
##    print(visions)
    return max(visions.values())
    
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
