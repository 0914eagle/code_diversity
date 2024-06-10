
def is_equal_to_sum_even(n: int) -> bool:
    
    # Check if n is a positive even number
    if n % 2 == 0 and n > 0:
        # Check if n can be written as the sum of 4 positive even numbers
        if n % 4 == 0:
            return True
        else:
            return False
    else:
        return False

