def prod_signs(arr):
    
    if not arr:
        return None
    return sum(abs(i) for i in arr) * (1 if all(i >= 0 for i in arr) else -1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
