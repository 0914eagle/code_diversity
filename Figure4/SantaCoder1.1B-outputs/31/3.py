def is_prime(n):
    
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    elif n % 3 == 0:
        return False
    elif n % 5 == 0:
        return False
    else:
        for i in range(5, int(n ** 0.5) + 1, 6):
            if n % i == 0:
                return False
        return True


