
def f1(y, l):
    # find the largest base b such that y written in base b contains only decimal digits
    for b in range(y, 100):
        if all(int(i) in range(10) for i in str(y)):
            return b
    return -1

def f2(y, l):
    # find the largest base b such that y written in base b is at least l when interpreted as a number in base 10
    for b in range(y, 100):
        if int(str(y), b) >= l:
            return b
    return -1

if __name__ == '__main__':
    y, l = map(int, input().split())
    print(f2(y, l))

