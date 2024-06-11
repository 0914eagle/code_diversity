def largest_prime_factor(n: int):
    
    "*** YOUR CODE HERE ***"
    largest = 0
    for i in range(2, n + 1):
        if n % i == 0:
            largest = i
            n = n // i
            break
    return largest


