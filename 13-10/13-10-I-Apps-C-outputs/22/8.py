
def f(x, base):
    if x == 0:
        return 0
    else:
        return (x % base) * 10**(len(str(x)) - 1) + f(x // base, base)

def solve(base, n):
    for x in range(1, int(2**63)):
        if f(x, base) == n:
            return x
    return "impossible"

if __name__ == '__main__':
    base, n = map(int, input().split())
    print(solve(base, n))

