
def is_equal_to_sum_even(n: int) -> bool:
    
    if n % 2 != 0:
        return False
    total = 0
    count = 0
    while total < n:
        total += 2
        count += 1
        if count == 4:
            return True
    return False

