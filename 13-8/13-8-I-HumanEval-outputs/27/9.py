
def is_equal_to_sum_even(n: int) -> bool:
    
    if n < 4 or n % 2 == 1:
        return False
    else:
        return all(n % i == 0 for i in range(2, int(n**0.5) + 1, 2))

