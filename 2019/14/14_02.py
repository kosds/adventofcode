import itertools
import cmath
import re

tests = [
##'''10 ORE => 10 A
##1 ORE => 1 B
##7 A, 1 B => 1 C
##7 A, 1 C => 1 D
##7 A, 1 D => 1 E
##7 A, 1 E => 1 FUEL''',
##'''9 ORE => 2 A
##8 ORE => 3 B
##7 ORE => 5 C
##3 A, 4 B => 1 AB
##5 B, 7 C => 1 BC
##4 C, 1 A => 1 CA
##2 AB, 3 BC, 4 CA => 1 FUEL''',
##'''157 ORE => 5 NZVS
##165 ORE => 6 DCFZ
##44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
##12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
##179 ORE => 7 PSHF
##177 ORE => 5 HKGWZ
##7 DCFZ, 7 PSHF => 2 XJWVT
##165 ORE => 2 GPVTF
##3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT''',
##'''2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
##17 NVRVD, 3 JNWZP => 8 VPVL
##53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
##22 VJHF, 37 MNCFX => 5 FWMGM
##139 ORE => 4 NVRVD
##144 ORE => 7 JNWZP
##5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
##5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
##145 ORE => 6 MNCFX
##1 NVRVD => 8 CXFTF
##1 VJHF, 6 MNCFX => 4 RFSQX
##176 ORE => 6 VJHF''',
'''171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX'''
  ]

oreammount = 1000000000000

def parsechem(line):
    num, el = line.strip().split(' ')
    return el, int(num)

def parsereactlist(line):
    reacts = {}
    for react in line.strip().split('\n'):
        reactsplit = react.strip().split('=>')
        res = parsechem(reactsplit[-1])
        ingrids = []
        for elem in reactsplit[0].strip().split(','):
            ingrids.append(parsechem(elem))
        reacts[res[0]] = {'ammount': res[1], 'ingrids': tuple(ingrids)}
##    print(reacts)
    return reacts

def proc(line):
    reactions = parsereactlist(line)
    got = {'ORE': oreammount}
    need = {'FUEL': 1}
    fuel = 0 
    fuelprocessed = True
    for elem in reactions:
        got[elem] = 0
    print(got)
    oreenough = True
    steps = []
    cycled = False
    while fuelprocessed:
        notenough = True
        while notenough:
##            print('n=', need)
##            print('g=', got)
            notenough = False
            for elem, num_need in list(need.items()):
                 if got[elem] < need[elem] and need[elem] != 0:
                    if elem == 'ORE':
                        oreenough = False
                        break
                    notenough = True
                    num_from_react = reactions[elem]['ammount']
                    num_reacts = (need[elem] - got[elem] - 1) // num_from_react + 1
                    got[elem] += num_from_react * num_reacts - need[elem]
                    need[elem] = 0
                    for ingrid in reactions[elem]['ingrids']:
                        if ingrid[0] in need:
                            need[ingrid[0]] += ingrid[1] * num_reacts
                        else:
                            need[ingrid[0]] = ingrid[1] * num_reacts
        if oreenough:
##            need2 = {a: b for a,b in need.items() if b>0}

            
##            if not cycled:
##                step = set()
##                for elem in got:
##                    if elem in need:
##                        needel = need[elem]
##                    else:
##                        needel = 0
##                    if elem != 'ORE':
##                        elemtostep = (elem, needel, got[elem])
##                    else:
##                        elemtostep = (elem, needel)
##                    step.add(elemtostep)    
##                if fuel == 0:
##                    step0 = step.copy()
##                else:
##                    if step == step0:
##                        print('FOUND CYCLE: ', len(steps), fuel)
####                        orebycycle = sum([sum([el[1] for el in step if el[0]=='ORE'])
####                                          for step in steps])
####                        print(orebycycle)
####                        print(oreammount - got['ORE'])
##                        orebycycle = oreammount - got['ORE']
##                        num_cycles = oreammount // orebycycle - 1
##                        fuel += fuel * num_cycles
##                        got['ORE'] -= orebycycle * num_cycles
##                        print(fuel)
##                        print(got)
##                        cycled = True


##            if not cycled:
##                step = set()
##                for elem in got:
##                    if elem in need:
##                        needel = need[elem]
##                    else:
##                        needel = 0
##                    if elem != 'ORE':
##                        elemtostep = (elem, needel, got[elem])
##                    else:
##                        elemtostep = (elem, needel)
##                    step.add(elemtostep)    
##                if len(steps) > 0 and step in steps:
##                        print('FOUND CYCLE: ', len(steps), fuel)
####                        orebycycle = sum([sum([el[1] for el in step if el[0]=='ORE'])
####                                          for step in steps])
####                        print(orebycycle)
####                        print(oreammount - got['ORE'])
##                        orebycycle = oreammount - got['ORE']
##                        num_cycles = oreammount // orebycycle - 1
##                        fuel += fuel * num_cycles
##                        got['ORE'] -= orebycycle * num_cycles
##                        print(fuel)
##                        print(got)
##                        cycled = True   
##                else:
##                    steps.append(step.copy())
                    
##            steps.append(step.copy())            
##            print('need =', need)
##            print('need =', need2)
##            print(step)
##            print('got  =', got)
            
##            print('got  =', got)
            for elem in need:
                got[elem] -= need[elem]
            fuel += 1
            need = {'FUEL': 1}
            if fuel % 400000 == 0:
                print(fuel)
                print(got)
##            print(need)
        else:
            fuelprocessed = False
    print('fuel=', fuel)
    print(got)
    return fuel
        
                    
            
##            notenough = not all([elem in got and got[elem] > need[elem] for elem in need])
                    
                    
                        
        
##        for elem in list(need.keys()):
##            if elem == 'ORE':
##                continue
##            num_need = need[elem]
##            if num_need > 0:
##                reactgoes = True
##                num_from_react = reactions[elem]['ammount']
##                num_reacts = (num_need - 1) // num_from_react + 1
##                need[elem] -= num_reacts * num_from_react
##                for ingrid in reactions[elem]['ingrids']:
##                    if ingrid[0] in need:
##                        need[ingrid[0]] += ingrid[1] * num_reacts
##                    else:
##                        need[ingrid[0]] = ingrid[1] * num_reacts
##            gotfuel += 1
##    print(need['ORE'])
####    print(gotfuel)
##    cycles = oreammount // need['ORE']
##    need = {a: b*cycles for a, b in need.items()}
##    need['ORE'] -= oreammount
##    gotfuel = cycles
##    print('cycles', cycles)
####    print(need)
##    reactgoes = True
##    while reactgoes:
##        if need['FUEL'] == 0:
##            need['FUEL'] += 1
##        reactgoes = False
##        for elem in list(need.keys()):
##            go = True
##            if elem == 'ORE':
##                continue
##            num_need = need[elem]
##            if num_need > 0:     
##                num_from_react = reactions[elem]['ammount']
##                num_reacts = (num_need - 1) // num_from_react + 1
##                if 'ORE' in [elem[0] for elem in reactions[elem]['ingrids']]:
##                    res = tuple(filter(lambda x: x[0]=='ORE', reactions[elem]['ingrids']))
##                    if need['ORE'] + ingrid[1] * num_reacts > 0:
####                        print('pass')
##                        go = False
##                        continue
##                if go:
##                    need[elem] -= num_reacts * num_from_react
##                    if elem
##                    for ingrid in reactions[elem]['ingrids']:
##                        need[ingrid[0]] += ingrid[1] * num_reacts
##                        reactgoes = True 
##        if gotfuel % 100000 == 0:
##            print(gotfuel)
##            print(need)
##    print(need)
##    print(gotfuel)
##    return gotfuel   
            

def main():
    for test in tests:
        res = proc(test)
        print('output =', res)
        print()
    with open('input14.txt') as f:
        res = proc(f.read())
        print('output =', res)
        print()

        
if __name__ == '__main__':
    main()
