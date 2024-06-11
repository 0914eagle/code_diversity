def prod_signs(arr):
    
    if not arr:
        return None
    return sum(map(abs, arr)) * reduce(lambda x, y: x * y, map(sign, arr))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/02_algorithms/01_recursion