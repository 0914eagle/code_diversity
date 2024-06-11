def prod_signs(arr):
    
    if not arr:
        return None
    prod = 1
    for num in arr:
        if num > 0:
            prod *= 1
        elif num < 0:
            prod *= -1
        else:
            prod *= 0
    return sum(abs(num) * prod for num in arr)


if