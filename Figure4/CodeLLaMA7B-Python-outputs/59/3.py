def largest_prime_factor(n: int):
    
    "*** YOUR CODE HERE ***"
    largest_prime = 1
    while n % 2 == 0:
        largest_prime = 2
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            largest_prime = i
            n = n // i
    if n > 2:
        largest_prime = n
    return largest_prime


