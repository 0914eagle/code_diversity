def largest_prime_factor(n: int):
    
    factor = 2
    while factor <= n:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1
    return factor

if __name__ == "__main__":
    import doctest
    doctest.testmod()
/python/problem_001.py
"""
Multip