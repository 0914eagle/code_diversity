
n = int(input())
p = list(map(int, input().split()))

def get_cyclic_shift(p, k):
    return [p[i-k] for i in range(n)]

def get_deviation(p):
    return sum(abs(p[i] - i) for i in range(n))

min_deviation = get_deviation(p)
optimal_shift = 0

for k in range(n):
    shifted = get_cyclic_shift(p, k)
    deviation = get_deviation(shifted)
    if deviation < min_deviation:
        min_deviation = deviation
        optimal_shift = k

print(min_deviation, optimal_shift)

