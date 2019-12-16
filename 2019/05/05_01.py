oldtest = ['3,9,8,9,10,9,4,9,99,-1,8',
         '3,9,7,9,10,9,4,9,99,-1,8',
         '3,3,1108,-1,8,3,4,3,99',
         '3,3,1107,-1,8,3,4,3,99',
           '3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9',
         '3,3,1105,-1,9,1101,0,0,12,4,12,99,1']

tests = ['3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99' ]       

def summ(a,b):
    return a + b

def mul(a,b):
    return a * b

def le(a,b):
    return a < b

def eq(a,b):
    return a == b

def get(c, line, i, pos):
##    print(c[i], line, i, pos)
    if c[i] == 0:
        return line[line[pos+i+1]]
    if c[i] == 1:
        return line[pos+i+1]

def proc(line):
    line =list(map(int, line.split(',')))
##    print(line)
##    line[1] = n
##    line[2] = v
    pos = 0
    output = ''
    while True:
        codeline = line[pos]
        code = codeline % 100
        codeline = codeline // 100
        param = []
        for _ in range(3):
            param.append(codeline % 10)
            codeline //= 10
        print(line[pos], code, param)
        if code == 99:
            break
        elif code == 1:
            func = summ
        elif code == 2:
            func = mul
        elif code == 3:
           line[line[pos+1]] = int(input())
        elif code == 4:
            output += str(get(param, line, 0, pos))
##            print(output)
        elif code == 5:
            jump = get(param, line, 0, pos) > 0
##            print(get(param, line, 0, pos), jump)
        elif code == 6:
            jump = get(param, line, 0, pos) == 0
        elif code == 7:
            func = le
        elif code == 8:
            func = eq
        else:
            print('ERROR!', line[pos])
            break
        if code in (1,2):
            print(get(param, line, 0, pos),get(param, line, 1, pos))
            line[line[pos+3]] = func(get(param, line, 0, pos),
                                get(param, line, 1, pos))
            pos += 4
        if code in (3,4):
            pos += 2
        if code in (5,6):
            if jump:
                pos = get(param, line, 1, pos)
                print(pos)
            else:
                pos += 3
        if code in (7,8):
            boo = func(get(param, line, 0, pos),
                        get(param, line, 1, pos))
            line[line[pos+3]] = 1 if boo else 0
            pos += 4
##        print(line)
    return output

def cycleproc(line):
    line =list(map(int, line.split(',')))
    print(line)
    res = proc(l)
 
            

def main():
##    for test in tests:
##        res = proc(test)
##        print('output =', res)
##        print()
    with open('input05.txt') as f:
        res = proc(f.read())
        print(res)

if __name__ == '__main__':
    main()
