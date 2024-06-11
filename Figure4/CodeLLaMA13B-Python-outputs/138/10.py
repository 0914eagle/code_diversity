def is_equal_to_sum_even(n):
    
    if n == 0:
        return False
    if n == 2:
        return True
    if n % 2 != 0:
        return False
    return is_equal_to_sum_even(n - 2)


