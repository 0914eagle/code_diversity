
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
            subarray = arr[:i] + arr[i + 1:]
            if is_increasing(subarray):
                max_len = max(max_len, len(subarray))
        return max_len

    if is_increasing(a):
        return n

    return max(find_max_length(a), find_max_length(a[::-1]))

print(max_increasing_subarray_length(n, a))
