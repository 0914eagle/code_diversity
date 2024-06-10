
def get_input():
    n = int(input())
    weights = list(map(int, input().split()))
    return n, weights

def find_min_diff(n, weights):
    min_diff = float('inf')
    for t in range(1, n):
        s1 = sum(weights[:t])
        s2 = sum(weights[t:])
        diff = abs(s1 - s2)
        if diff < min_diff:
            min_diff = diff
    return min_diff

def main():
    n, weights = get_input()
    print(find_min_diff(n, weights))

if __name__ == '__main__':
    main()

