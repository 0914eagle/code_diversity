def pluck(arr):
    
    if not arr:
        return []

    min_val = min(arr)
    min_index = arr.index(min_val)
    if min_val % 2 == 0:
        return [min_val, min_index]

    for i in range(len(arr)):
        if arr[i] % 2 == 0 and arr[i] < min_val:
            min_val = arr[i]
            min_index = i

    return [min_val, min_index]
