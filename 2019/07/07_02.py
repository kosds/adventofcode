import itertools

oldtest = ['3,9,8,9,10,9,4,9,99,-1,8',
         '3,9,7,9,10,9,4,9,99,-1,8',
         '3,3,1108,-1,8,3,4,3,99',
         '3,3,1107,-1,8,3,4,3,99',
           '3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9',
         '3,3,1105,-1,9,1101,0,0,12,4,12,99,1']

tests = ['3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5',
         '3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10']

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

def proc(line, pos, inpt):
    line =list(map(int, line.split(',')))
##    print(line)
##    line[1] = n
##    line[2] = v
##    pos = state[1]
    output = ''
    while True:
        codeline = line[pos]
        code = codeline % 100
        codeline = codeline // 100
        param = []
        for _ in range(3):
            param.append(codeline % 10)
            codeline //= 10
##        print(line[pos], code, param)
        if code == 99:
            break
        elif code == 1:
            func = summ
        elif code == 2:
            func = mul
        elif code == 3:
##            print('got!')
##           line[line[pos+1]] = int(input())
            line[line[pos+1]] = inpt.pop()
        elif code == 4:
            output += str(get(param, line, 0, pos))
##            print(output)
            state = (','.join(map(str,line)), pos + 2)
            return int(output), state
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
##            print(get(param, line, 0, pos),get(param, line, 1, pos))
            line[line[pos+3]] = func(get(param, line, 0, pos),
                                get(param, line, 1, pos))
            pos += 4
        if code in (3,4):
            pos += 2
        if code in (5,6):
            if jump:
                pos = get(param, line, 1, pos)
##                print(pos)
            else:
                pos += 3
        if code in (7,8):
            boo = func(get(param, line, 0, pos),
                        get(param, line, 1, pos))
            line[line[pos+3]] = 1 if boo else 0
            pos += 4
##        print(line)
##    return int(output)

def cycleproc(line):
    signalmax, bestsetup = 0, ()
    for phasesec in itertools.permutations(range(5,10)):
        signal_end = -1
        signal = 0
##        print(phasesec)
        amp = []
        for phase in phasesec:
            amp.append([line, 0, phase])
        first = True
        while signal_end != signal:
            signal_end = signal
##            print(signal_end)
##        for _ in range(5):
            for i in range(5):
                if first:
                    inpt = [signal, amp[i][2]]
                else:
                    inpt = [signal]
##            print(inpt)
                try:
                    signal, state = proc(amp[i][0], amp[i][1], inpt)
                    amp[i][0], amp[i][1] = state
                except:
                    pass
            first = False
##            signal_end = signal
##            print(signal_end)
##            print(signal, phasesec)
        if signal > signalmax:
##            print('got!')
            bestsetup = phasesec
            signalmax = signal
    return signalmax, bestsetup
##    line =list(map(int, line.split(',')))
##    print(line)
##    res = 
 
            

def main():
    for test in tests:
        res = cycleproc(test)
        print('output =', res)
        print()
    with open('input07.txt') as f:
        res = cycleproc(f.read())
        print('output =', res)
        print()
if __name__ == '__main__':
    main()
