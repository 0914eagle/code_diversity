def prod_signs(arr):
    
    if not arr:
        return None
    return sum([abs(x) for x in arr]) * (-1) ** (len(arr) - 1)


if __name__ == "__main__":
    import doctest

    doctest.test