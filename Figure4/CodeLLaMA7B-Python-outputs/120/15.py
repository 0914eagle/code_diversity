def maximum(arr, k):
    
    if k == 0: return []
    if k == 1: return [max(arr)]
    if k == len(arr): return sorted(arr)

    # find the k-th largest number
    # use quick sort to partition the array
    # the k-th largest number will be at the (len(arr) - k)th position
    