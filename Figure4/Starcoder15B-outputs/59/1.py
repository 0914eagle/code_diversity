def largest_prime_factor(n: int):
    
    largest_factor = 1
    for i in range(2, n):
        if n % i == 0:
            largest_factor = i
            n //= i
    return largest_factor

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/problem_0002.py
"""
Each new term in the