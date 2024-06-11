def pluck(arr):
    
    if not arr:
        return []

    min_value = min(arr)
    min_index = arr.index(min_value)

    if min_value % 2 == 0:
        return [min_value, min_index]

    return []
