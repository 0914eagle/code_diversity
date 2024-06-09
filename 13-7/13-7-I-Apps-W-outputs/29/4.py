
def solve(arr):
    n = len(arr) // 2
    left, right = arr[:n], arr[n:]
    if sum(left) == sum(right):
        return "-1"
    return " ".join(str(x) for x in arr)

