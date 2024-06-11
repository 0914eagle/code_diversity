def largest_prime_factor(n: int):
    
    prime_factor = 1
    for i in range(2, n):
        if n % i == 0:
            prime_factor = i
    return prime_factor


if __name__ == "__main__":
    import doctest

    doctest.testmod()
