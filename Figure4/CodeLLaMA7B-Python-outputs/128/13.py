def prod_signs(arr):
    
    if not arr:
        return None
    return sum(abs(i) for i in arr) * (-1) ** (len(arr) // 2)


if __name__