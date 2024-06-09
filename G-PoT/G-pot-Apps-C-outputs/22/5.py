
from fractions import Fraction

N, Q = map(int, input().split())
stones = [0] * N
total_stones = 0
total_squares = 0

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        u, v = query[1], query[2]
        for i in range(u-1, v):
            total_squares -= stones[i] ** 2
            stones[i] += 1
            total_squares += stones[i] ** 2
            total_stones += 1
    else:
        expected_value = Fraction(total_squares, total_stones ** 2)
        print(expected_value % (10**9 + 7))

