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
K)L''']
    

def proc(line):
    orbits = {}
    lines =list(line.split('\n'))
    for lin in lines:
        if lin:
            a, b = lin.split(')')
            orbits[b] = [a, 0]
    root = set(a[0] for a in orbits.values()) - set(orbits.keys())
    print(orbits, root)
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
                res += orbits[pl[0]][1]
##                print(orbits[pl[0]], res)
    return res          
            

def main():
    for test in tests:
        res = proc(test)
        print('output =', res)
        print()
    with open('input06.txt') as f:
        res = proc(f.read())
        print(res)

if __name__ == '__main__':
    main()
