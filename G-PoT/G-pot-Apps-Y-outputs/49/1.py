
n = int(input())
a = list(map(int, input().split()))

def max_increasing_subarray_length(n, a):
    def check_increasing(arr):
        for i in range(len(arr) - 1):
            if arr[i] >= arr[i + 1]:
                return False
        return True

    max_len = 1
    for i in range(n):
        if i > 0 and i < n - 1 and a[i - 1] < a[i + 1]:
            max_len = max(max_len, 2)
            l, r = i - 1, i + 1
            while l > 0 and a[l - 1] < a[l]:
                l -= 1
                max_len = max(max_len, r - l + 1)
            while r < n - 1 and a[r] < a[r + 1]:
                r += 1
                max_len = max(max_len, r - l + 1)
        else:
            l, r = i, i
            while l > 0 and a[l - 1] < a[l]:
                l -= 1
                max_len = max(max_len, r - l + 1)
            while r < n - 1 and a[r] < a[r + 1]:
                r += 1
                max_len = max(max_len, r - l + 1)

    return max_len

print(max_increasing_subarray_length(n, a))
