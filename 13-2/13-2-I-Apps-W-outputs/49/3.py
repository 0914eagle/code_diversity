
def get_max_median(arr, k):
    n = len(arr)
    arr.sort()
    median = arr[n//2]
    for i in range(k):
        for j in range(n):
            if arr[j] < median:
                arr[j] += 1
                median = max(median, arr[j])
                break
    return median

