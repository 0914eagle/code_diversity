def prod_signs(arr):
    
    if not arr:
        return None
    res = 0
    for i in arr:
        if i > 0:
            res += 1
        elif i < 0:
            res -= 1
    return res * arr[0] * arr[0]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
