
def is_valid_test_case(n, a, b):
    if a == b:
        return "Yes"
    
    for k in range(1, n // 2 + 1):
        a_prefix = a[:k]
        a_suffix = a[k:]
        if a_prefix == a_suffix:
            continue
        a_prefix.reverse()
        a_suffix.reverse()
        a = a_prefix + a_suffix
        if a == b:
            return "Yes"
    
    return "No"

