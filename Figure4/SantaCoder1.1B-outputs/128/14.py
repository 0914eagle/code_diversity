def prod_signs(arr):
    
    if not arr:
        return None
    mag = 0
    for i in arr:
        mag += i * (1 if i > 0 else -1)
    return mag * prod_signs(arr[1:])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
