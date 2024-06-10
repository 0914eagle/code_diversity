
def get_weights():
    return list(map(int, input().split()))

def get_min_abs_diff(weights, t):
    s1 = sum(weights[:t])
    s2 = sum(weights[t:])
    return abs(s1 - s2)

def main():
    weights = get_weights()
    n = len(weights)
    min_diff = float('inf')
    for t in range(1, n):
        diff = get_min_abs_diff(weights, t)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

if __name__ == '__main__':
    main()

