
def f1(n, s):
    # find the smallest b such that f(b, n) = s
    for b in range(2, 1000000000):
        if f2(b, n) == s:
            return b
    return -1

def f2(b, n):
    # compute f(b, n)
    if n < b:
        return n
    else:
        return f2(b, n // b) + (n % b)

if __name__ == '__main__':
    n, s = map(int, input().split())
    print(f1(n, s))

