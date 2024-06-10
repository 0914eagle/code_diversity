
def get_pairs_with_power(a, k):
    pairs = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] * a[j] == k:
                pairs += 1
    return pairs

def solve(n, k, a):
    return get_pairs_with_power(a, k)

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))

