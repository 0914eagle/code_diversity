
def is_equal_to_sum_even(n: int) -> bool:
    
    if n % 2 != 0:
        return False
    n //= 2
    count = 0
    while n > 0:
        count += 1
        n -= 2
    return count == 4

