def prod_signs(arr):
    
    if not arr:
        return None
    prod = 1
    for i in arr:
        if i == 0:
            prod *= 0
        elif i > 0:
            prod *= 1
        else:
            prod *= -1
    return sum(map(abs, arr)) * prod


if __name__ == "__main