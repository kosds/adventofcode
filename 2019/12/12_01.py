import itertools
import cmath
import re


oldtest = ['3,9,8,9,10,9,4,9,99,-1,8',
         '3,9,7,9,10,9,4,9,99,-1,8',
         '3,3,1108,-1,8,3,4,3,99',
         '3,3,1107,-1,8,3,4,3,99',
           '3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9',
         '3,3,1105,-1,9,1101,0,0,12,4,12,99,1']

tests = [
'''<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>'''
  ]

steps = 10

def applygravity(m1, m2):
    for i in range(3):
        p1 = m1['pos'][i]
        p2 = m2['pos'][i]
        if p1 != p2:
            dif = (p2 - p1 > 0) * 2 - 1
            m1['vel'][i] += dif
            m2['vel'][i] -= dif
            
def applyvelocity(moon):
    for i in range(3):
        moon['pos'][i] += moon['vel'][i]

def calcenergy(moon):
    pot = sum(map(abs, moon['pos']))
    kin = sum(map(abs, moon['vel']))
    return pot * kin

def proc(line):
    moons = []
    line = line.split('\n')
    for lin in line:
        x,y,z = map(int,
                    re.match(r'<x=([-\d]*), y=([-\d]*), z=([-\d]*)>', lin).
                        group(1,2,3))
        moons.append({'pos': [x,y,z], 'vel': [0,0,0]})
    print(moons)
    for step in range(steps):
        for i, moon1 in enumerate(moons[:-1]):
            for j, moon2 in enumerate(moons[i+1:]):
                applygravity(moon1, moon2)
        for moon in moons:
            applyvelocity(moon)
        energy = sum([calcenergy(moon) for moon in moons])
        print(step, moons, energy)
    print()

def main():
    for test in tests:
        res = proc(test)
        print('output =', res)
        print()
    with open('input12.txt') as f:
        res = proc(f.read())
        print('output =', res)
        print()

        
if __name__ == '__main__':
    main()
