
def solve(arr):
    n = len(arr)
    if n == 1:
        return "YES"
    if n == 2:
        if arr[0] < arr[1]:
            return "YES"
        else:
            return "NO"
    if n == 3:
        if arr[0] < arr[1] + arr[2] and arr[1] < arr[2] + arr[0] and arr[2] < arr[0] + arr[1]:
            return "YES"
        else:
            return "NO"
    # General case
    for i in range(n):
        left_sum = arr[i-1] if i > 0 else 0
        right_sum = arr[i+1] if i < n-1 else 0
        if arr[i] > left_sum + right_sum:
            return "NO"
    return "YES"

