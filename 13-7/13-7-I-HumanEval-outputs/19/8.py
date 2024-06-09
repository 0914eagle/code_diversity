
def is_equal_to_sum_even(n: int) -> bool:
    
    if n % 2 == 1:
        return False
    else:
        return any(n == i + j for i in range(2, n//2+1, 2) for j in range(2, n//2+1, 2))

