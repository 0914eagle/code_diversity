def prod_signs(arr):
    
    if not arr:
        return None
    mag = 0
    prod = 1
    for i in arr:
        if i == 0:
            continue
        mag += i
        prod *= i
    return mag * prod


