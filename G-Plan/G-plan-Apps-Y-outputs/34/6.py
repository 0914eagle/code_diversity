
def count_operations(arr, k):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    min_num = min(arr)
    max_num = max(arr)
    min_ops = float('inf')

    for target in range(min_num, max_num + 1):
        ops = 0
        for num, count in freq.items():
            diff = abs(num - target)
            ops += diff * count if num > target else (diff + 1) * count

        if ops < min_ops and sum(count for num, count in freq.items() if num >= target) >= k:
            min_ops = ops

    return min_ops

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(count_operations(arr, k))
