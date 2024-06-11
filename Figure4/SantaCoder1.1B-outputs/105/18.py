def by_length(arr):
    
    if not arr:
        return []
    arr.sort()
    arr = [name for name in names if name in arr]
    arr.reverse()
    return arr


