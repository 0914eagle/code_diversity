
def solve(n, k, a):
    left, right = 0, n - 1
    count = 0
    while left <= right:
        if a[left] <= k:
            count += 1
            left += 1
        if a[right] <= k:
            count += 1
            right -= 1
        if left <= right:
            count += 1
            left += 1
            right -= 1
    return count

