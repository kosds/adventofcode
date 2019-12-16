tests = [
'''R8,U5,L5,D3
U7,R6,D4,L4''',
'''R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83''',
'''R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'''
]       


size = 20001

def run(grid, path, pos, inter, check=True, printg=False):
    path = path.split(',')
    pathlen = 0
    for move in path:
        disp = int(move[1:])
        if move[0] == 'R':
            for y in range(pos[1] + 1, pos[1] + disp + 1):
                pathlen += 1
                if check:
                    if grid[pos[0]][y] > 1:
                        inter.append(pathlen + grid[pos[0]][y])
                else:
                    
                    if grid[pos[0]][y] == 0:
                        grid[pos[0]][y] = pathlen
            pos[1] += disp
        if move[0] == 'L':
            for y in range(pos[1] - 1, pos[1] - disp - 1, -1):
                pathlen += 1
                if check:
                    if grid[pos[0]][y] > 0:
                        inter.append(pathlen + grid[pos[0]][y])
                else:  
                    if grid[pos[0]][y] == 0:
                        grid[pos[0]][y] = pathlen
            pos[1] -= disp
        if move[0] == 'U':
            for x in range(pos[0] - 1, pos[0] - disp - 1, - 1):
                pathlen += 1
                if check:
                    if grid[x][pos[1]] > 0:
                        inter.append(pathlen + grid[x][pos[1]])
                else:

                    if grid[x][pos[1]] == 0:
                        grid[x][pos[1]] = pathlen
            pos[0] -= disp
        if move[0] == 'D':
            for x in range(pos[0] + 1, pos[0] + disp + 1):
                pathlen += 1
                if check:
                    if grid[x][pos[1]] > 0:
                        inter.append(pathlen + grid[x][pos[1]])
                else:
                    
                    if grid[x][pos[1]] == 0:
                        grid[x][pos[1]] = pathlen
            pos[0] += disp
    if printg:
        for st in grid:
            for el in st:
                print(el if el>0 else '.', end='   ')
            print()
            
                    
def proc(line):
    grid = []
    for i in range(size):
        grid.append([0] * size)
    center = size // 2
    paths = line.split('\n')
    inter = []
    print(paths)
    checked = False
    for path in paths:
        run(grid, path, [center,center], inter, check=checked,printg=False)
        checked = True
    print(inter)
    res = min(inter)
    print(res)
    
def main():
    for test in tests:
        proc(test)
        print()
    with open('input03.txt') as f:
        proc(f.read())

if __name__ == '__main__':
    main()
