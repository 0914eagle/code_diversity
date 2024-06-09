
def max_sum_after_k_swap(arr, k):
    n = len(arr)
    if k == 0:
        return sum(arr)
    if n == 1:
        return arr[0]
    if k == 1:
        return max(arr[0], arr[1])
    if k == 2:
        return max(arr[0], arr[1], arr[2])
    if k == 3:
        return max(arr[0], arr[1], arr[2], arr[3])
    if k == 4:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4])
    if k == 5:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])
    if k == 6:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6])
    if k == 7:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7])
    if k == 8:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8])
    if k == 9:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9])
    if k == 10:
        return max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9], arr[10])


