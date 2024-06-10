
def get_f(x, base):
    return sum(int(i) * base ** (len(str(x)) - ix - 1) for ix, i in enumerate(str(x)))

def solve(base, n):
    for x in range(1, n + 1):
        if get_f(x, base) == n:
            return x
    return "impossible"

if __name__ == '__main__':
    base, n = map(int, input().split())
    print(solve(base, n))

