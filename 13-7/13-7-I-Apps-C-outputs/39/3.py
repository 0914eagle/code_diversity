
def get_max_sum(arr):
    n = len(arr) // 2
    arr.sort()
    return sum(arr[:n]) + sum(arr[n:])

