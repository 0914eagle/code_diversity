def by_length(arr):
    
    if not arr:
        return []
    arr = sorted(arr)
    arr = [name for name, num in zip(names, arr) if num >= 1 and num <= 9]
    return arr


