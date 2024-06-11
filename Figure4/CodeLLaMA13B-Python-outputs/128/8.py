def prod_signs(arr):
    
    if len(arr) == 0:
        return None
    prod = 1
    for i in arr:
        if i == 0:
            prod = 0
            break
        elif i < 0:
            prod *= -1
    return sum(abs(i) for i in arr) * prod


if