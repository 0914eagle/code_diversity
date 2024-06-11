def prod_signs(arr):
    
    if not arr:
        return None
    return sum(abs(x) for x in arr) * (-1)**sum(x < 0 for x in arr)


