
def f(b, n):
    if n < b:
        return n
    else:
        return f(b, n // b) + (n % b)

def solve(n, s):
    for b in range(2, 1000000000):
        if f(b, n) == s:
            return b
    return -1

if __name__ == '__main__':
    n, s = map(int, input().split())
    print(solve(n, s))

