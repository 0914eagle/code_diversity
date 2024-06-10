
def calculate_partition_sum(arr, c):
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]

    min_sum = float('inf')
    for i in range(1, n + 1):
        min_sum = min(min_sum, prefix_sum[i] - min(i // c, n) * min(arr[:i]))

    return min_sum

if __name__ == "__main__":
    n, c = map(int, input().split())
    arr = list(map(int, input().split()))
    print(calculate_partition_sum(arr, c))
