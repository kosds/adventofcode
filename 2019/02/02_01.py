tests = ['1,0,0,0,99',
'2,3,0,3,99',
'2,4,4,5,99,0',
'1,1,1,4,99,5,6,0,99']       

def summ(a,b):
    return a + b

def mul(a,b):
    return a * b

def proc(line):
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
    return line

def main():
    for i, test in enumerate(tests):
        print('== Test {} =='.format(i))
        code =list(map(int, test.split(',')))
        print(proc(code))
    with open('input02.txt') as f:
        print('== Mainpart ==')
        code =list(map(int, f.read().strip().split(',')))
        code[1] = 12
        code[2] = 2
        line = proc(code)
        print('result =', line[0])


if __name__ == '__main__':
    main()
