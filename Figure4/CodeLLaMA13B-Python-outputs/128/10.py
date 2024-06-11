def prod_signs(arr):
    
    if not arr:
        return None

    signs = [1 if i > 0 else -1 if i < 0 else 0 for i in arr]
    signs_prod = 1
    for i in signs:
        signs_prod *= i

    arr_abs = [abs(i) for i in arr]
    arr_abs_prod = 1
    for i in arr_abs:
        arr_abs_prod *= i

    return arr_abs_prod * signs_prod


if