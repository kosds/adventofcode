from collections import Counter

inter = [372037, 905157]
                                
def proc(inter):
    res = 0
    for num in range(inter[0], inter[1] + 1):
        s = str(num)
        c = Counter(s)
        if ''.join(sorted(s)) == s and any((valc in (2,) for valc in c.values())):
##            print(num)
            res += 1
    print('passwords =', res)
    
def main():
    proc(inter)

if __name__ == '__main__':
    main()
