

def is_multiply_prime(a):
    
    if a >= 100:
        return False

    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                if i * j * k == a:
                    if is_prime(i) and is_prime(j) and is_prime(k):
                        return True

    return False

def
