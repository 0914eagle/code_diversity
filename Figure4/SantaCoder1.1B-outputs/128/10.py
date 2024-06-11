def prod_signs(arr):
    
    if not arr:
        return None

    prod = 1
    for i in arr:
        prod *= i

    res = 0
    for i in arr:
        if i == 0:
            res += 0
        elif i == 1:
            res += 1
        else:
            res += -1

    return prod * res


