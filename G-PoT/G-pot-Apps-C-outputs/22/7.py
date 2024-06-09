
import math

N, Q = map(int, input().split())
stones = [0] * N
total_sum = 0
total_squares = 0

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        u, v = query[1], query[2]
        for i in range(u-1, v):
            total_squares -= stones[i] ** 2
            stones[i] += 1
            total_squares += stones[i] ** 2
    else:
        total_sum += total_squares

    if total_sum == 0:
        print(0)
    else:
        gcd = math.gcd(total_sum, N)
        print((total_sum * pow(N, 10**9 + 6 - 2, 10**9 + 7) // gcd) % (10**9 + 7))
