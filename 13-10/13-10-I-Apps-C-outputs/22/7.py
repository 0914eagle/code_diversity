
def f(n, b):
    if n == 0:
        return 0
    else:
        return (n % b) * 10 ** (len(str(n)) - 1) + f(n // b, b)

def solve(b, n):
    for i in range(1, n + 1):
        if f(i, b) == n:
            return i
    return "impossible"

if __name__ == '__main__':
    b, n = map(int, input().split())
    print(solve(b, n))

