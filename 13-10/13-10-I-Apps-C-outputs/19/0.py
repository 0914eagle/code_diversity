
def max_sum_after_k_swaps(arr, k):
    n = len(arr)
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + arr[i]
    max_sum = 0
    for i in range(n):
        for j in range(i + 1, n):
            max_sum = max(max_sum, prefix_sums[j + 1] - prefix_sums[i])
    for _ in range(k):
        i, j = 0, 0
        while i == j or i + 1 == j or j + 1 == i:
            i = random.randint(0, n - 1)
            j = random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
        prefix_sums[i + 1], prefix_sums[j + 1] = prefix_sums[j + 1], prefix_sums[i + 1]
        max_sum = max(max_sum, prefix_sums[j + 1] - prefix_sums[i])
    return max_sum

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_sum_after_k_swaps(arr, k))

if __name__ == '__main__':
    main()

