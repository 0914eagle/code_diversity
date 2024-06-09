
n = int(input())
a = list(map(int, input().split()))

def max_increasing_subarray_length(n, a):
    def is_increasing(arr):
        for i in range(len(arr) - 1):
            if arr[i] >= arr[i + 1]:
                return False
        return True

    def find_max_length(arr):
        max_len = 1
        for i in range(len(arr)):
            if i > 0 and i < len(arr) - 1:
                if arr[i - 1] < arr[i + 1]:
                    max_len = max(max_len, i + 1)
                if arr[i - 1] < arr[i] < arr[i + 1]:
                    max_len = max(max_len, i + 2)
        return max_len

    if is_increasing(a):
        return n

    max_len = find_max_length(a)
    for i in range(1, n - 1):
        if a[i - 1] < a[i + 1]:
            max_len = max(max_len, find_max_length(a[:i] + a[i + 1:]))
    
    return max_len

print(max_increasing_subarray_length(n, a))
