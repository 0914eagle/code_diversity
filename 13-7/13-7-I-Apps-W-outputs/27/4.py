
def solve(arr):
    n = len(arr)
    if n == 1:
        return "YES"
    for i in range(n):
        left = (i - 1) % n
        right = (i + 1) % n
        if arr[i] >= arr[left] + arr[right]:
            return "NO"
    return "YES"

