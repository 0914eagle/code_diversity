def is_equal_to_sum_even(n):
    
    if n == 0:
        return False
    if n == 2:
        return True
    if n % 2 == 1:
        return False
    if n % 4 == 0:
        return True
    return is_equal_to_sum_even(n - 2)


