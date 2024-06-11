def is_equal_to_sum_even(n):
    
    if n % 2 != 0:
        return False
    if n == 0:
        return True
    return is_equal_to_sum_even(n - 2) or is_equal_to_sum_even(n - 4) or is_equal_to_sum_even(n - 6) or is_equal_to_sum_even(n - 8)


