def prod_signs(arr):
    
    if not arr:
        return None
    return sum(abs(i) for i in arr) * (-1 if any(i < 0 for i in arr) else 1)


