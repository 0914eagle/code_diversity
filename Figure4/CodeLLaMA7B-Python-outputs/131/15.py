def digits(n):
    
    prod = 1
    while n > 0:
        if n % 2 == 1:
            prod *= n % 10
        n //= 10
    return prod


