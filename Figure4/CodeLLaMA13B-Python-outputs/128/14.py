def prod_signs(arr):
    
    if not arr:
        return None

    prod = 1
    for num in arr:
        if num:
            prod *= 1 if num > 0 else -1

    return sum(abs(num) * prod for num in arr)


if __name__