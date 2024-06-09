
def is_valid_test_case(n, a, b):
    if a == b:
        return "Yes"
    
    for k in range(1, n // 2 + 1):
        prefix = a[:k]
        suffix = a[n - k:]
        if prefix == suffix:
            continue
        if prefix == suffix[::-1]:
            a = a[:k] + suffix + a[k:]
            if a == b:
                return "Yes"
    
    return "No"
