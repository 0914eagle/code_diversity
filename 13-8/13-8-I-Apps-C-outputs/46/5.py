
def get_fibonacci_character(n, k):
    if n == 0:
        return "."
    elif n == 1:
        return "W"
    else:
        return get_fibonacci_character(n-1, k-1)

def solve(queries):
    result = []
    for query in queries:
        n, k = query
        result.append(get_fibonacci_character(n, k))
    return "".join(result)

if __name__ == '__main__':
    q = int(input())
    queries = []
    for i in range(q):
        n, k = map(int, input().split())
        queries.append((n, k))
    print(solve(queries))

