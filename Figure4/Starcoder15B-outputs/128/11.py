def prod_signs(arr):
    
    if not arr:
        return None
    prod = 1
    for num in arr:
        if num == 0:
            return 0
        if num < 0:
            prod *= -1
    return prod * sum(map(abs, arr))


