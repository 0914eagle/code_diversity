def is_equal_to_sum_even(n):
    
    if n % 2 == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n - i * 2 in range(2, n):
            return True
    return False


