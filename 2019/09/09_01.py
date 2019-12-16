import itertools

oldtest = ['3,9,8,9,10,9,4,9,99,-1,8',
         '3,9,7,9,10,9,4,9,99,-1,8',
         '3,3,1108,-1,8,3,4,3,99',
         '3,3,1107,-1,8,3,4,3,99',
           '3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9',
         '3,3,1105,-1,9,1101,0,0,12,4,12,99,1']

tests = [
##'109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99',
    '1102,34915192,34915192,7,4,7,99,0',
         '104,1125899906842624,99',
         '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'
    ]

def summ(a,b):
    return a + b

def mul(a,b):
    return a * b

def le(a,b):
    return a < b

def eq(a,b):
    return a == b

def get(c, line, i, pos, rel):
##    print(c[i], line, i, pos)
    if c[i] == 0:
##        print(line[pos+i+1])
        return line[line[pos+i+1]]
    if c[i] == 1:
##        print(line[pos+i+1])
        return line[pos+i+1]
    if c[i] == 2:
        return line[line[pos+i+1]+rel]

def proc(line):
    line =list(map(int, line.split(',')))
##    print(line)
##    line[1] = n
##    line[2] = v
##    pos = state[1]
    pos = 0
    output = ''
    rel_base = 0
    line += [0] * 10000
    while True:
        codeline = line[pos]
##        print(codeline)
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
            if param[0] == 0:
                line[line[pos+1]] = int(input())
            if param[0] == 2:
                line[line[pos+1] + rel_base] = int(input())
##            line[line[pos+1]] = inpt.pop()
        elif code == 4:
            output += str(get(param, line, 0, pos, rel_base)) + ' '
##            print(output)
            state = (','.join(map(str,line)), pos + 2)
##            return int(output), state
        elif code == 5:
            jump = get(param, line, 0, pos, rel_base) > 0
##            print(get(param, line, 0, pos, rel_base), jump)
        elif code == 6:
            jump = get(param, line, 0, pos, rel_base) == 0
        elif code == 7:
            func = le
        elif code == 8:
            func = eq
        elif code == 9:
            rel_base += get(param, line, 0, pos, rel_base)
        else:
            print('ERROR!', line[pos])
            break
        if code in (1,2):
##            print(get(param, line, 0, pos, rel_base),get(param, line, 1, pos))
            if line[pos+3] >= len(line):
                line += [0] * (line[pos+3] - len(line) + 10)
            if param[2] == 0:
                place = line[pos+3]
            if param[2] == 2:
                place = line[pos+3]+rel_base
            line[place] = func(get(param, line, 0, pos, rel_base),
                                get(param, line, 1, pos, rel_base))
            pos += 4
        if code in (3,4,9):
            pos += 2
        if code in (5,6):
            if jump:
                pos = get(param, line, 1, pos, rel_base)
##                print(pos)
            else:
                pos += 3
        if code in (7,8):
            boo = func(get(param, line, 0, pos, rel_base),
                        get(param, line, 1, pos, rel_base))
            if param[2] == 0:
                place = line[pos+3]
            if param[2] == 2:
                place = line[pos+3] + rel_base
            line[place] = 1 if boo else 0
            pos += 4
##        print(line)
    return output

##def cycleproc(line):
##    signalmax, bestsetup = 0, ()
##    for phasesec in itertools.permutations(range(5,10)):
##        signal_end = -1
##        signal = 0
####        print(phasesec)
##        amp = []
##        for phase in phasesec:
##            amp.append([line, 0, phase])
##        first = True
##        while signal_end != signal:
##            signal_end = signal
####            print(signal_end)
####        for _ in range(5):
##            for i in range(5):
##                if first:
##                    inpt = [signal, amp[i][2]]
##                else:
##                    inpt = [signal]
####            print(inpt)
##                try:
##                    signal, state = proc(amp[i][0], amp[i][1], inpt)
##                    amp[i][0], amp[i][1] = state
##                except:
##                    pass
##            first = False
####            signal_end = signal
####            print(signal_end)
####            print(signal, phasesec)
##        if signal > signalmax:
####            print('got!')
##            bestsetup = phasesec
##            signalmax = signal
##    return signalmax, bestsetup
##    line =list(map(int, line.split(',')))
##    print(line)
##    res = 
 
            

def main():
    for test in tests:
        res = proc(test)
        print('output =', res)
        print()
    with open('input09.txt') as f:
        res = proc(f.read())
        print('output =', res)
        print()
if __name__ == '__main__':
    main()
