def prod_signs(arr):
    
    if not arr:
        return None
    return sum(map(lambda x: abs(x), arr)) * prod_sign(arr)


