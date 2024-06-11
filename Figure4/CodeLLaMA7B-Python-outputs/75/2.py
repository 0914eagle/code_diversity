def is_multiply_prime(a):
    
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for prime in prime_list:
        if a % prime == 0:
            a = a / prime
        else:
            return False
    return True


