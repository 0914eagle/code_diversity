def is_multiply_prime(a):
    
    if a < 100:
        for i in range(2, 100):
            if is_prime(i) and is_prime(a / i) and is_prime(a / (i * (a / i))):
                return True
        return False
    else:
        return "Error: a is greater than 100"


