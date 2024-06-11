def largest_prime_factor(n: int):
    
    "*** YOUR CODE HERE ***"
    largest_prime_factor = 1
    for i in range(2, n + 1):
        if n % i == 0:
            largest_prime_factor = i
            n = n // i
            break
    return largest_prime_factor


