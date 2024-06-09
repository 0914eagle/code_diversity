
def solve(n, k, a):
    left, right = 0, n - 1
    count = 0
    while left >= 0 and right < n and a[left] <= k and a[right] <= k:
        count += 1
        if a[left] <= a[right]:
            left -= 1
        else:
            right += 1
    return count

