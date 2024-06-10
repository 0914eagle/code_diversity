
def is_multiply_prime(a: int) -> bool:
    
    if a < 100 and a > 0:
        i = 2
        while i * i <= a:
            if a % i == 0:
                j = 2
                while j * j <= (a // i):
                    if (a // i) % j == 0:
                        k = 2
                        while k * k <= (a // i // j):
                            if (a // i // j) % k == 0:
                                return False
                            k += 1
                        return True
                    j += 1
                return False
            i += 1
    return False

