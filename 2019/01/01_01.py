import math

tests = [12, 13, 1969, 100756]       

def proc(num):
    res = math.floor(num / 3) - 2
    return res

def parsefile(output):
    nums = list(map(int, output.split()))
    return sum(proc(num) for num in nums)
        
def main():
    for i, test in enumerate(tests):
        print('== Test {} =='.format(i))
        print('result =', proc(test))
        print()
    with open('input01.txt') as f:
        print('== Mainpart ==')
        print('result =', parsefile(f.read()))
        
if __name__ == '__main__':
    main()
