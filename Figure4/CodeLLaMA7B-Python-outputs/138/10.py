def is_equal_to_sum_even(n):
    
    if n % 2 != 0:
        return False
    else:
        for i in range(1, n):
            if i % 2 == 0:
                if n - i == 2 * i:
                    return True
    return False


