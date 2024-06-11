def prod_signs(arr):
    
    if not arr:
        return None
    return sum(abs(x) for x in arr) * (-1 if any(x < 0 for x in arr) else 1)


