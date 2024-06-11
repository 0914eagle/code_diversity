def prod_signs(arr):
    
    if not arr:
        return None
    prod = 1
    for i in arr:
        prod *= i if i else 1
    return sum([abs(i) * (1 if i > 0 else -1) for i in arr]) * prod


if __name__ == "__main__":
    print(prod_signs([1, 2, 2, -4]))
    print(prod_signs([0, 1]))
    print(prod_signs([]))
