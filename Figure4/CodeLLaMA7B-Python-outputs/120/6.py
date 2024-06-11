def maximum(arr, k):
    
    if k == 0: return []
    if k == 1: return [max(arr)]
    if k == len(arr): return sorted(arr)

    # find the kth largest number
    # use quick select algorithm
    # https://en.wikipedia.org/wiki/Quickselect
    