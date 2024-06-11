def prod_signs(arr):
    
    if not arr:
        return None
    return sum(abs(x) for x in arr) * (-1) ** (len(arr) // 2)


if __name__