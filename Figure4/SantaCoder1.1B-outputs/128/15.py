def prod_signs(arr):
    
    if not arr:
        return None
    arr = sorted(arr)
    prod = 1
    for i in range(len(arr)):
        if arr[i] == 0:
            prod *= -1
        elif arr[i] == 1:
            prod *= 1
        else:
            prod *= arr[i]
    return prod


