def by_length(arr):
    
    if not arr:
        return []
    arr = sorted(arr)
    arr = [f"{i}" for i in arr]
    arr = [i.title() for i in arr]
    return arr


