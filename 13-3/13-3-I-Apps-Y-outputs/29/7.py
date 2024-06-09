
def solve(n, k):
    if n % 2 == 0:
        return solve_even(n, k)
    else:
        return solve_odd(n, k)

def solve_even(n, k):
    a = []
    for i in range(k):
        a.append(n // (k - i))
        n %= (k - i)
        if n == 0:
            return "YES\n" + " ".join(str(x) for x in a)
    return "NO"

def solve_odd(n, k):
    a = []
    for i in range(k):
        a.append(n // (k - i) + 1)
        n %= (k - i)
        if n == 0:
            return "YES\n" + " ".join(str(x) for x in a)
    return "NO"

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(solve(n, k))

