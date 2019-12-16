##import itertools
##
##oldtest = ['3,9,8,9,10,9,4,9,99,-1,8',
##         '3,9,7,9,10,9,4,9,99,-1,8',
##         '3,3,1108,-1,8,3,4,3,99',
##         '3,3,1107,-1,8,3,4,3,99',
##           '3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9',
##         '3,3,1105,-1,9,1101,0,0,12,4,12,99,1']
##
tests = ['123456789012']

size = (25,6)
lenth = size[0] * size[1]

def proc(line):
    line = [int(a) for a in line]
    layers = []
    
    for i in range(0,len(line),lenth):
        layers.append(line[i:i+lenth])
    print(layers)
    a = min(layers, key=lambda a: a.count(0))
    return a.count(1) * a.count(2)

def main():
##    for test in tests:
##        res = proc(test)
##        print('output =', res)
##        print()
    with open('input08.txt') as f:
        res = proc(f.read().strip())
        print('output =', res)
        print()
if __name__ == '__main__':
    main()
