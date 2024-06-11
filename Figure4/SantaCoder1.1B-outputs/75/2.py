def is_multiply_prime(a):
    
    if a < 100:
        return False
    if a % 3 == 0:
        return True
    for i in range(5, int(a ** 0.5) + 1, 6):
        if a % i == 0:
            return False
    return True


