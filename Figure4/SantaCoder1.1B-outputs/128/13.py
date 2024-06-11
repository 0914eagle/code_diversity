def prod_signs(arr):
    
    if len(arr) == 0:
        return None
    arr.sort()
    prod = 1
    for i in range(len(arr)):
        if arr[i] == 0:
            continue
        if arr[i] == 1:
            prod *= 1
        else:
            prod *= -1
    return prod


