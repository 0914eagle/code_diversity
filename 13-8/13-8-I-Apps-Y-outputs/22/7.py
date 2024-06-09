
def solve(n, k, arr):
    left, right = 0, n-1
    count = 0
    while left >= 0 and right < n:
        if arr[left] <= k:
            count += 1
            left -= 1
        if arr[right] <= k:
            count += 1
            right += 1
        left -= 1
        right += 1
    return count

