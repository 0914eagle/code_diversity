
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
            if i == 0:
                max_len = max(max_len, 1 + (arr[i] < arr[i + 1]))
            elif i == len(arr) - 1:
                max_len = max(max_len, 1 + (arr[i - 1] < arr[i]))
            else:
                max_len = max(max_len, 1 + (arr[i - 1] < arr[i] < arr[i + 1]))
        return max_len

    max_len = 0
    for i in range(n):
        if i == 0:
            max_len = max(max_len, find_max_length(a[1:]))
        elif i == n - 1:
            max_len = max(max_len, find_max_length(a[:-1]))
        else:
            max_len = max(max_len, find_max_length(a[:i] + a[i+1:]))
    
    return max_len

print(max_increasing_subarray_length(n, a))
