
def get_prettiness(a, n):
    
    a.sort(reverse=True)
    if n == 1:
        return a[0]
    if n == 2:
        return a[0] + a[1]
    if n == 3:
        return a[0] + a[1] + a[2]
    if a[0] % a[1] == 0 or a[0] % a[2] == 0:
        return a[0] + a[1] + a[2]
    if a[1] % a[0] == 0 or a[1] % a[2] == 0:
        return a[0] + a[1] + a[2]
    if a[2] % a[0] == 0 or a[2] % a[1] == 0:
        return a[0] + a[1] + a[2]
    return a[0] + a[1] + a[2]

def solve(queries):
    for query in queries:
        n = int(query[0])
        a = list(map(int, query[1:]))
        print(get_prettiness(a, n))

if __name__ == '__main__':
    q = int(input())
    queries = [input().split() for _ in range(q)]
    solve(queries)

