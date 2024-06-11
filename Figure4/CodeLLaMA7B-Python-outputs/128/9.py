def prod_signs(arr):
    
    if not arr:
        return None
    res = 0
    for i in arr:
        if i > 0:
            res += 1
        elif i < 0:
            res -= 1
        else:
            res += 0
    return res * (abs(reduce(lambda x, y: x * y, arr)) if arr else 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
