
def count_operations(arr, target, k):
    operations = 0
    for num in arr:
        diff = 0
        while num > target:
            num //= 2
            diff += 1
        if num == target:
            operations += diff
    return operations

def min_operations_to_equal(arr, k):
    min_val = min(arr)
    max_val = max(arr)
    min_operations = float('inf')
    for target in range(min_val, max_val + 1):
        operations = count_operations(arr, target, k)
        if operations < min_operations:
            min_operations = operations
    return min_operations

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(min_operations_to_equal(arr, k))
