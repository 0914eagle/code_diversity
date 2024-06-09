
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve_query(N, queries):
    stones = [0] * N
    total_stones = 0
    total_squares = 0
    for query in queries:
        if query[0] == 1:
            u, v = query[1], query[2]
            for i in range(u-1, v):
                total_squares -= stones[i] ** 2
                stones[i] += 1
                total_squares += stones[i] ** 2
                total_stones += 1
        else:
            numerator = total_squares * total_stones
            denominator = N * (N + 1) // 2
            common_divisor = gcd(numerator, denominator)
            print((numerator // common_divisor) * pow(denominator // common_divisor, 10**9 + 6, 10**9 + 7) % (10**9 + 7))

N, Q = map(int, input().split())
queries = []
for _ in range(Q):
    query = list(map(int, input().split()))
    queries.append(query)

solve_query(N, queries)
