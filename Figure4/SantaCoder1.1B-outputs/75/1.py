def is_multiply_prime(a):
    
    if a < 100:
        return False
    if a % 3 == 0:
        return True
    if a % 5 == 0:
        return True
    return False

