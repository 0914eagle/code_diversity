
def f1(l, d, n):
    return l - n * d - 6 * n

def f2(l, d, n):
    return (l - 6 * n - d) // (d + 1)

if __name__ == '__main__':
    l, d, n = map(int, input().split())
    print(f1(l, d, n))
    print(f2(l, d, n))

