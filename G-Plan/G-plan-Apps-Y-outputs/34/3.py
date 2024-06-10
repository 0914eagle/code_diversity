
def count_operations(arr, k):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    min_op = float('inf')
    for target in range(min(arr), max(arr) + 1):
        ops = 0
        for num, freq in freq.items():
            diff = abs(num - target)
            ops += diff * freq
        min_op = min(min_op, ops)
    
    return min_op

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(count_operations(arr, k))
