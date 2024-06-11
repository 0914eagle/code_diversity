def largest_prime_factor(n: int):
    
    "*** YOUR CODE HERE ***"
    largest = 0
    i = 2
    while i ** 2 <= n:
        while n % i == 0:
            largest = i
            n = n // i
        i += 1
    if n > 1:
        largest = n
    return largest


