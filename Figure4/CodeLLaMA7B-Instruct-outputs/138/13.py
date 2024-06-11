

def is_equal_to_sum_even(n):
    
    if n % 2 != 0 or n < 4:
        return False
    for i in range(2, n+1, 2):
        if n == i * 4:
            return True
    return False

