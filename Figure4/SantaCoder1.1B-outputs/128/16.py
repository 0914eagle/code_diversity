def prod_signs(arr):
    
    if not arr:
        return None
    return sum(map(lambda x: abs(x), arr)) * prod_signs(arr[1:])


if __name__ == "__main__":
    import doctest

    doctest.