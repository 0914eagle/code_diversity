
def solve(n, k):
    if n % 2 == 0:
        return solve_even(n, k)
    else:
        return solve_odd(n, k)

def solve_even(n, k):
    a = []
    while n > 0:
        a.append(n % 2)
        n //= 2
    a.sort(reverse=True)
    return a[:k]

def solve_odd(n, k):
    a = []
    while n > 0:
        a.append(n % 2 + 1)
        n //= 2
    a.sort(reverse=True)
    return a[:k]

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print("YES" if solve(n, k) else "NO")

