def is_equal_to_sum_even(n):
    
    if n % 2 != 0:
        return False
    else:
        return is_equal_to_sum_even_helper(n, 0, 0, 0, 0)


