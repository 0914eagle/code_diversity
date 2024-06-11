def is_equal_to_sum_even(n):
    
    if n % 2 == 1:
        return False
    if n == 8:
        return True
    for i in range(2, n // 2 + 1):
        if is_equal_to_sum_even(n - i) and i % 2 == 0:
            return True
    return False


