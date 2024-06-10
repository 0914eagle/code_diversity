
def get_weights():
    n = int(input())
    weights = list(map(int, input().split()))
    return n, weights

def get_min_abs_diff(weights, t):
    s1, s2 = 0, 0
    for i in range(t):
        s1 += weights[i]
    for i in range(t, len(weights)):
        s2 += weights[i]
    return abs(s1 - s2)

def solve():
    n, weights = get_weights()
    min_abs_diff = float('inf')
    for t in range(1, n):
        abs_diff = get_min_abs_diff(weights, t)
        if abs_diff < min_abs_diff:
            min_abs_diff = abs_diff
    return min_abs_diff

if __name__ == '__main__':
    print(solve())

