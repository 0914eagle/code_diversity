
def solve_recurrence(a, x, t, m):
    if t == 0:
        return x[0] % m
    else:
        return (a[0] + sum(a[i] * x[t-i] for i in range(1, len(a)))) % m

def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        t, m = map(int, input().split())
        print(solve_recurrence(a, x, t, m))

if __name__ == "__main__":
    main()

