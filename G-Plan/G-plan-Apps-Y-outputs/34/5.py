
def count_operations(arr, k):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    min_ops = float('inf')
    for target in range(min(arr), max(arr) + 1):
        ops = 0
        for num, count in freq.items():
            diff = abs(num - target)
            ops += diff * count // k
        
        min_ops = min(min_ops, ops)
    
    return min_ops

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(count_operations(arr, k))
