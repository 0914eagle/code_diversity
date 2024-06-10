
def get_min_abs_diff(weights):
    n = len(weights)
    min_abs_diff = float('inf')
    for t in range(1, n):
        s1 = sum(weights[:t])
        s2 = sum(weights[t:])
        abs_diff = abs(s1 - s2)
        if abs_diff < min_abs_diff:
            min_abs_diff = abs_diff
    return min_abs_diff

def main():
    n = int(input())
    weights = list(map(int, input().split()))
    print(get_min_abs_diff(weights))

if __name__ == '__main__':
    main()

