def largest_prime_factor(n: int):
    
    largest = 1
    for i in range(2, n + 1):
        if n % i == 0:
            largest = i
            n = n // i
    return largest


