def is_equal_to_sum_even(n):
    
    if n % 2 == 0:
        return False
    if n % 4 == 0:
        return False
    if n % 6 == 0:
        return False
    if n % 8 == 0:
        return True
    return False


