
def find_max_average(arr, k):
    n = len(arr)
    if n == 0:
        return 0
    if k > n:
        return 0
    max_sum = 0
    current_sum = 0
    for i in range(n):
        current_sum += arr[i]
        if i >= k-1:
            max_sum = max(max_sum, current_sum)
            current_sum -= arr[i-k+1]
    return max_sum/k

