def is_multiply_prime(a):
    
    if a < 100:
        for i in range(2, 100):
            if is_prime(i):
                for j in range(2, 100):
                    if is_prime(j):
                        for k in range(2, 100):
                            if is_prime(k):
                                if i * j * k == a:
                                    return True
        return False


