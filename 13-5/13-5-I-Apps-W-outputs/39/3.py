
def is_valid_test_case(a, b):
    n = len(a)
    for i in range(1, int(n/2)+1):
        if a[:i] == b[n-i:] and a[i:] == b[:n-i]:
            return True
    return False

