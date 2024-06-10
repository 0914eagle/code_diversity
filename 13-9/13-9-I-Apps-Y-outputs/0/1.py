
def get_input():
    n = int(input())
    weights = list(map(int, input().split()))
    return n, weights

def find_min_diff(n, weights):
    min_diff = float('inf')
    for t in range(1, n):
        group1 = weights[:t]
        group2 = weights[t:]
        diff = abs(sum(group1) - sum(group2))
        if diff < min_diff:
            min_diff = diff
    return min_diff

def main():
    n, weights = get_input()
    print(find_min_diff(n, weights))

if __name__ == '__main__':
    main()

