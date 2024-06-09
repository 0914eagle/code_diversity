
n = int(input())
p = list(map(int, input().split()))

def get_deviation(p):
    deviation = 0
    for i in range(n):
        deviation += abs(p[i] - i)
    return deviation

def get_cyclic_shift(p, k):
    return [p[i] for i in range(k, n+k)] + [p[i] for i in range(k)]

def get_min_deviation_cyclic_shift(p):
    min_deviation = get_deviation(p)
    min_deviation_cyclic_shift = p
    for k in range(n):
        cyclic_shift = get_cyclic_shift(p, k)
        deviation = get_deviation(cyclic_shift)
        if deviation < min_deviation:
            min_deviation = deviation
            min_deviation_cyclic_shift = cyclic_shift
    return min_deviation, min_deviation_cyclic_shift

min_deviation, min_deviation_cyclic_shift = get_min_deviation_cyclic_shift(p)
print(min_deviation)
print(min_deviation_cyclic_shift.index(1) if 1 in min_deviation_cyclic_shift else -1)

