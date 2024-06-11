def by_length(arr):
    
    if not arr:
        return []
    arr = sorted(arr)
    arr = [name for name, _ in sorted(zip(names, range(10)))]
    return arr


