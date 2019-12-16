import math     

def proc(num):
    res = math.floor(num / 3) - 2
    return res

def parsefile(output):
    nums = list(map(int, output.split()))
    res2 = 0
    for num in nums:
        res = proc(num)
        while res > 0:
            res2 += res
            res = proc(res)
    return res2

def main():
    with open('input01.txt') as f:
        print('== Mainpart ==')
        print('result =', parsefile(f.read()))

if __name__ == '__main__':
    main()
