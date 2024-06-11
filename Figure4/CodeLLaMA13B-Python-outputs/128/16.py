def prod_signs(arr):
    
    if not arr:
        return None
    prod = 1
    for num in arr:
        prod *= 1 if num > 0 else -1 if num < 0 else 0
    return sum(abs(num) * prod for num in arr)


if __name__ == "__main__":
    print(prod_signs([