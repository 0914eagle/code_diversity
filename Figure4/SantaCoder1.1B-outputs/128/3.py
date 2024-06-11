def prod_signs(arr):
    
    if not arr:
        return None
    return sum(abs(x) * (1 if x > 0 else -1) for x in arr)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
