
def get_max_sum(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr[0], arr[1])
    if n % 2 == 0:
        return max(arr[0] + arr[2], arr[1] + arr[3])
    return max(arr[0] + arr[2] + arr[4], arr[1] + arr[3] + arr[5])

