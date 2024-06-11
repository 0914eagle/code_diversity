def maximum(arr, k):
    
    if not arr or k == 0:
        return []

    arr.sort()
    return arr[-k:]


