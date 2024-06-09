
import sys

def f(r, c):
    if r == 0 or c == 0:
        return 1
    elif r == 1 and c == 1:
        return 2
    else:
        return (f(r-1, c) + f(r, c-1)) % (10**9+7)

def solve(r1, c1, r2, c2):
    return sum(f(i, j) for i in range(r1, r2+1) for j in range(c1, c2+1)) % (10**9+7)

if __name__ == '__main__':
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
    print(solve(r1, c1, r2, c2))

