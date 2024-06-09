
def solve(n, k):
    if n % 2 == 0:
        return solve_even(n, k)
    else:
        return solve_odd(n, k)

def solve_even(n, k):
    a = [2] * k
    for i in range(k):
        a[i] += 2 * i
    if sum(a) == n:
        return "YES\n" + " ".join(map(str, a))
    else:
        return "NO"

def solve_odd(n, k):
    a = [1] * k
    for i in range(k):
        a[i] += 2 * i + 1
    if sum(a) == n:
        return "YES\n" + " ".join(map(str, a))
    else:
        return "NO"

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(solve(n, k))

