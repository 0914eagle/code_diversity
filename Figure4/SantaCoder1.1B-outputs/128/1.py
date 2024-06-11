def prod_signs(arr):
    
    if not arr:
        return None
    return sum(map(lambda x: x * (1 if x > 0 else -1), arr))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
