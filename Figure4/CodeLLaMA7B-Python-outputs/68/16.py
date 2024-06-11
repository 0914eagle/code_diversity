def pluck(arr):
    
    if not arr:
        return []

    min_val = min(arr)
    min_index = arr.index(min_val)

    if min_val % 2 == 0:
        return [min_val, min_index]

    return []
