
n = int(input())
p = list(map(int, input().split()))

def get_deviation(p):
    deviation = 0
    for i in range(n):
        deviation += abs(p[i] - i)
    return deviation

def get_cyclic_shift(p, k):
    return [p[i] for i in range(n) if i % n == k]

def get_optimal_cyclic_shift(p):
    min_deviation = float('inf')
    optimal_shift = None
    for k in range(n):
        shift = get_cyclic_shift(p, k)
        deviation = get_deviation(shift)
        if deviation < min_deviation:
            min_deviation = deviation
            optimal_shift = shift
    return optimal_shift

optimal_shift = get_optimal_cyclic_shift(p)
print(get_deviation(optimal_shift), get_cyclic_shift(p, optimal_shift.index(1)))

