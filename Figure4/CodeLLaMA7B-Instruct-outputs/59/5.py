


def largest_prime_factor(n: int):
    
    if n % 2 == 0:
        if n > 2:
            return 2
        else:
            return 1
    for i in range(int(n ** 0.5), 1, -1):
        if n % i == 0 and is_prime(i):
            return i
    return 1


def is_prime
