def prod_signs(arr):
    
    if not arr:
        return None
    return sum(abs(x) for x in arr) * prod(sign(x) for x in arr)


if __name__ == '__main__':