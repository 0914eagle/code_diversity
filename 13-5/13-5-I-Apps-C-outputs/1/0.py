
def f1(y, l):
    # Find the largest base b such that y written in base b contains only decimal digits
    for b in range(y, 10):
        if all(int(i) in range(10) for i in str(y)):
            return b
    return 10

def f2(y, l):
    # Find the largest base b such that y written in base b is at least l when interpreted as a number in base 10
    for b in range(y, 10):
        if int(str(y), b) >= l:
            return b
    return 10

if __name__ == '__main__':
    y, l = map(int, input().split())
    print(f2(y, l))

