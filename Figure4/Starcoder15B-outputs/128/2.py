def prod_signs(arr):
    
    if not arr:
        return None
    return sum(map(abs, arr)) * reduce(lambda x, y: x * y, map(sign, arr))


