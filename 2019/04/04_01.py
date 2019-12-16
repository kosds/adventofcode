inter = [372037, 905157]
                   
def proc(inter):
    res = 0
    for num in range(inter[0], inter[1] + 1):
        s = str(num)
        if ''.join(sorted(s)) == s and len(set(s)) < 6:
##            print(num)
            res += 1
    print('passwords =', res)
    
def main():
    proc(inter)
    print()

if __name__ == '__main__':
    main()
