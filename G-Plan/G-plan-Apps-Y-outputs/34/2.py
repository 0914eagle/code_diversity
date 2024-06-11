
def count_operations(arr, k):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    min_val = min(arr)
    max_val = max(arr)
    min_ops = float('inf')

    for target in range(min_val, max_val + 1):
        ops = 0
        for num, count in freq.items():
            diff = abs(num - target)
            ops += diff * count
            if num < target:
                ops += (target - num) * count
            else:
                ops += diff * count

        if sum(count for num, count in freq.items() if num < target) >= k:
            min_ops = min(min_ops, ops)

    return min_ops

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(count_operations(arr, k))