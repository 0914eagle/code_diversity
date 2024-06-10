
def get_input():
    n = int(input())
    weights = list(map(int, input().split()))
    return n, weights

def get_sum(weights, t):
    return sum(weights[:t])

def get_min_abs_diff(weights):
    n = len(weights)
    min_abs_diff = float('inf')
    for t in range(1, n):
        s1 = get_sum(weights, t)
        s2 = get_sum(weights, n - t)
        abs_diff = abs(s1 - s2)
        if abs_diff < min_abs_diff:
            min_abs_diff = abs_diff
    return min_abs_diff

def main():
    n, weights = get_input()
    print(get_min_abs_diff(weights))

if __name__ == '__main__':
    main()

