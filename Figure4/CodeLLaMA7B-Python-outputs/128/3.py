def prod_signs(arr):
    
    if not arr:
        return None
    return sum(abs(i) for i in arr) * (-1) ** (len(arr) - arr.count(0))


if __name__ == "__main__":
    import doctest

    doct