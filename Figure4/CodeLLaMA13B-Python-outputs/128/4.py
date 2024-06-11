def prod_signs(arr):
    
    if len(arr) == 0:
        return None

    prod = 1
    for num in arr:
        prod *= num if num else 1

    return sum(map(abs, arr)) * prod


if __name__ == "__main__":
    assert prod_signs([1, 2, 2, -