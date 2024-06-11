def prod_signs(arr):
    
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr[0]
    else:
        return sum(arr) * prod([1 if i > 0 else -1 if i < 0 else 0 for i in arr])


if