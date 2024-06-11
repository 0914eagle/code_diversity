def by_length(arr):
    
    if not arr:
        return []
    arr = sorted(arr)
    arr = [name for name in names if name in arr]
    return arr


