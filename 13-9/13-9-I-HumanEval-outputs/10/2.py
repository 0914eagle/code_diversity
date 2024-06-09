
def is_equal_to_sum_even(n: int) -> bool:
    
    if n % 2 == 1:
        return False
    else:
        sum_of_four = n // 4
        return sum_of_four % 2 == 0

