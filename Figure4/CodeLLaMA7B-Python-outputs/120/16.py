def maximum(arr, k):
    
    if k == 0: return []
    if k == 1: return [max(arr)]
    if k == len(arr): return sorted(arr)

    arr.sort()
    return arr[-k:]

