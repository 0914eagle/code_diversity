
import itertools

def f1(n):
    return n * (n - 1) // 2

def f2(n, t):
    s = set(t)
    return len(s)

if __name__ == '__main__':
    n = int(input())
    t = list(map(int, input().split()))
    print(f2(n, t) % (10**9 + 7))

