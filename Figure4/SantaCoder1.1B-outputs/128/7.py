def prod_signs(arr):
    
    if not arr:
        return None

    result = 0
    for i in arr:
        result += i * prod_sign(i)
    return result


