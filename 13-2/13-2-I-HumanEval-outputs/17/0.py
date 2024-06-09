
def is_multiply_prime(a: int) -> bool:
    
    if a < 100 and a > 0:
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                j = a // i
                if is_prime(i) and is_prime(j):
                    return True
    return False

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

