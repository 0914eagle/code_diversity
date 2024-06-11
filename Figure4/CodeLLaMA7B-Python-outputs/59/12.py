def largest_prime_factor(n: int):
    
    "*** YOUR CODE HERE ***"
    largest = 0
    for i in range(2, n + 1):
        if n % i == 0:
            largest = i
            n //= i
            while n % i == 0:
                n //= i
            i = 2
    return largest


