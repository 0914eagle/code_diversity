def largest_prime_factor(n: int):
    
    "*** YOUR CODE HERE ***"
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
        else:
            i += 1
    return n


