
def is_equal_to_sum_even(n: int) -> bool:
    
    if n % 2 != 0 or n < 4:
        return False
    else:
        return sum(i for i in range(2, n+1, 2) if n % i == 0) == 4

