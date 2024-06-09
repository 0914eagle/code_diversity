
def solve(n, k):
    if n % 2 == 0:
        return solve_even(n, k)
    else:
        return solve_odd(n, k)

def solve_even(n, k):
    a = [2] * k
    for i in range(k):
        a[i] += n - sum(a)
    return a

def solve_odd(n, k):
    a = [1] * k
    for i in range(k):
        a[i] += n - sum(a)
    return a

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = solve(n, k)
        if a is not None:
            print("YES")
            print(*a)
        else:
            print("NO")

