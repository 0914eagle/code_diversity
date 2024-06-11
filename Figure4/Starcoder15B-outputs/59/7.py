def largest_prime_factor(n: int):
    
    largest_prime = 1
    for i in range(2, n):
        if n % i == 0:
            largest_prime = i
    return largest_prime

