
def f1(n):
    return int(str(n).replace('1', '9').replace('9', '1'))

def f2(n):
    return int(str(n).translate({ord('1'): '9', ord('9'): '1'}))

if __name__ == '__main__':
    n = int(input())
    print(f1(n))
    print(f2(n))

