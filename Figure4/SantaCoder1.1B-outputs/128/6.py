def prod_signs(arr):
    
    if not arr:
        return None
    return sum(map(lambda x: x * (1 if x > 0 else -1), arr))


