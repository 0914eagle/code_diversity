
def is_equal_to_sum_even(n: int) -> bool:
    
    if n % 2 != 0:
        return False
    total = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            total += i
            if total == n:
                return True
    return False

