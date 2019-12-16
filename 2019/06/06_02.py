tests = [
'''COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
''']
    

def proc(line):
    orbits = {}
    lines =list(line.split('\n'))
    clin = len(lines)
    for lin in lines:
        if lin:
            a, b = lin.split(')')
            orbits[b] = [a, 0]
    root = set(a[0] for a in orbits.values()) - set(orbits.keys())
##    print(orbits, root)
    queue = [root.pop()]
    res = 0
    print(queue)
    for el in queue:
        for pl in orbits.items():
##            print(pl, pl[1][0])
            if pl[1][0] == el:
                queue.append(pl[0])
                if el in orbits:
                    orbits[pl[0]][1] = orbits[el][1] + 1
                else:
                    orbits[pl[0]][1] = 1
##                res += orbits[pl[0]][1]
##                print(orbits[pl[0]], res)
    print(orbits['YOU'], orbits['SAN'])
    youpl = 'YOU'
    sanpl = 'SAN'
    for _ in range(orbits['YOU'][1] - orbits['SAN'][1]):
        youpl = orbits[youpl][0]
        res += 1
    print(orbits[youpl], orbits['SAN'], res)
    while youpl != sanpl:
        youpl = orbits[youpl][0]
        sanpl = orbits[sanpl][0]
        res += 2
    return res - 2         
            

def main():
    for test in tests:
        res = proc(test)
        print('output =', res)
        print()
    with open('input06.txt') as f:
        res = proc(f.read())
        print('output =', res)

if __name__ == '__main__':
    main()
