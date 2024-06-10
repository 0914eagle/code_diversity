
def is_multiply_prime(a: int) -> bool:
    
    if a < 100 and a > 0:
        i = 2
        while i * i <= a:
            if a % i == 0:
                j = 2
                while j * j <= a // i:
                    if a // i == j or a // (i * j) == 1:
                        return True
                    j += 1
            i += 1
    return False

