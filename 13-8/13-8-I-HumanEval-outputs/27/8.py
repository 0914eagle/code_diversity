
def is_equal_to_sum_even(n: int) -> bool:
    
    if n % 2 == 1:
        return False
    for i in range(2, int(n/2)):
        if i * 2 == n:
            return True
    return False

