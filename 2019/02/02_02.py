output = 19690720

def summ(a,b):
    return a + b

def mul(a,b):
    return a * b

def proc(line, n, v):
    line[1] = n
    line[2] = v
    for pos in range(0,len(line),4):
        if line[pos] == 99:
            break
        elif line[pos] == 1:
            func = summ
        elif line[pos] == 2:
            func = mul
        else:
            raise ValueError
        line[line[pos+3]] = func(line[line[pos+1]],
                                line[line[pos+2]])
    return line[0]

def cycleproc(line):
    line =list(map(int, line.split(',')))
    for noun in range(0,100):
        for verb in range(0,100):
            l = line.copy()
            res = proc(l, noun, verb)
            if res == output:
                return noun * 100 + verb
            
def main():
    with open('input02.txt') as f:
        res = cycleproc(f.read())
        print(res)

if __name__ == '__main__':
    main()
