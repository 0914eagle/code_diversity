
def get_return_days(p, n):
    days = [0] * n
    for i in range(n):
        days[i] = days[p[i] - 1] + 1
    return days

def solve(queries):
    for query in queries:
        n = int(query[0])
        p = [int(i) for i in query[1:]]
        days = get_return_days(p, n)
        print(*days)

if __name__ == '__main__':
    solve([input().split() for _ in range(int(input()))])

