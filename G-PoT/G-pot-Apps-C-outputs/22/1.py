
import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def calculate_expected_value(N, queries):
    stones = [0] * N
    total_stones = 0
    total_squares = 0

    for query in queries:
        if query[0] == 1:
            for i in range(query[1]-1, query[2]):
                stones[i] += 1
                total_stones += 1
        else:
            for stone_count in stones:
                total_squares += stone_count ** 2

            gcd_val = gcd(total_squares, total_stones ** 2)
            numerator = total_squares // gcd_val
            denominator = (total_stones ** 2) // gcd_val

            print((numerator * pow(denominator, 10**9 + 6, 10**9 + 7)) % (10**9 + 7))

N, Q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(Q)]

calculate_expected_value(N, queries)
