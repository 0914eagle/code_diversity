def prod_signs(arr):
    
    if not arr:
        return None
    prod = 1
    sum = 0
    for i in arr:
        if i > 0:
            prod *= 1
        elif i < 0:
            prod *= -1
        else:
            prod *= 0
        sum += abs(i)
    return sum * prod


if