
def f1(l, d, n):
    return l - n * d - 6 * 2

def f2(l, d, n):
    return l - n * d - 6 * 2

if __name__ == '__main__':
    l, d, n = map(int, input().split())
    print(f1(l, d, n))

