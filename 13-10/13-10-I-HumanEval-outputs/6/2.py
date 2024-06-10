
def is_multiply_prime(a: int) -> bool:
    
    # Check if a is less than 100
    if a >= 100:
        return False
    
    # Check if a is a multiple of 3, 5, or 7
    if a % 3 == 0 or a % 5 == 0 or a % 7 == 0:
        return True
    else:
        return False

