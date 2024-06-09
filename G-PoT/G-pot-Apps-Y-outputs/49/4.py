
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
        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:
                left_len = i
                break
            max_len += 1
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] >= arr[i + 1]:
                right_len = len(arr) - i - 1
                break
            max_len += 1
        if arr[left_len - 1] < arr[right_len + left_len]:
            max_len = max(max_len, left_len + right_len)
        return max_len

    if is_increasing(a):
        return n

    max_len = 1
    for i in range(1, n - 1):
        if a[i - 1] < a[i + 1]:
            max_len = max(max_len, find_max_length(a[:i] + a[i+1:]))
    
    return max_len

print(max_increasing_subarray_length(n, a))
