def largest_prime_factor(n: int):
    
    factor = 2
    while factor <= n:
        if n % factor == 0:
            n = n // factor
        else:
            factor += 1
    return factor


if __name__ == "__main__":
    import doctest
    doctest