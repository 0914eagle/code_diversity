def prod_signs(arr):
    
    if not arr:
        return None

    signs = [1 if x > 0 else -1 if x < 0 else 0 for x in arr]
    signs_prod = 1
    for x in signs:
        signs_prod *= x

    return sum(abs(x) * signs_prod for x in arr)


if