def is_multiply_prime(a):
    
    if a < 100:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True


