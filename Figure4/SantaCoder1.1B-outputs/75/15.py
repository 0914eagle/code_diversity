def is_multiply_prime(a):
    
    if a < 100:
        return False
    else:
        for i in range(2, a):
            if a % i == 0:
                return False
        return True

