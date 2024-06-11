def by_length(arr):
    
    if not arr:
        return []
    arr = sorted(arr)
    arr = [name for name, _ in sorted(enumerate(arr), key=lambda x: x[1])]
    return arr


