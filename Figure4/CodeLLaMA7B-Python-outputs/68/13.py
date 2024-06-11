def pluck(arr):
    
    if not arr:
        return []

    min_val = min(arr)
    if min_val % 2 == 0:
        return [min_val, arr.index(min_val)]

    return []
