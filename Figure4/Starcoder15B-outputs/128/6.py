def prod_signs(arr):
    
    if not arr:
        return None
    prod = 1
    for i in arr:
        if i == 0:
            return 0
        if i < 0:
            prod *= -1
    return prod * sum(map(abs, arr))


