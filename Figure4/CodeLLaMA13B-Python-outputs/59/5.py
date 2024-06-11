def largest_prime_factor(n: int):
    
    # Hint: start with i = 2 and use the algorithm from the previous problem.
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
        else:
            i += 1
    return n


if __name__ == "__main__":
    import doctest

    doctest.testmod()
