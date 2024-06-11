def prod_signs(arr):
    
    if not arr:
        return None
    res = 0
    for i in arr:
        if i == 0:
            res += 1
        elif i == 1:
            res += -1
        elif i == -1:
            res += 1
        else:
            res += 0
    return res


