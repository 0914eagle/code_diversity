def prod_signs(arr):
    
    if not arr:
        return None
    signs = [1 if i > 0 else -1 if i < 0 else 0 for i in arr]
    return sum(abs(i) for i in arr) * reduce(lambda x, y: x * y, signs)


