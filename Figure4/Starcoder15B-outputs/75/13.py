def is_multiply_prime(a):
    
    if a < 100:
        for i in range(2, a):
            if a % i == 0:
                if is_prime(i) and is_prime(a / i):
                    return True
    return False


