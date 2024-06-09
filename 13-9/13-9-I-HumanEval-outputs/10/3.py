
def is_equal_to_sum_even(n: int) -> bool:
    
    if n < 4 or n % 2 == 1:
        return False
    return all(n >= i * (i + 1) for i in range(1, 5))

