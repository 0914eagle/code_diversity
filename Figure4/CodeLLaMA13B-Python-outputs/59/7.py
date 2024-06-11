def largest_prime_factor(n: int):
    
    # Hint: start with the largest prime factor and divide by it.
    # If the remainder is 0, return the current factor.
    # If the remainder is 1, try the next largest factor.
    # If the remainder is greater than 1, divide by the remainder.
    # Repeat until the remainder is 1.
    # If the current factor is greater than the largest factor,
    # set the largest factor to the current factor.
    # Hint: you can use is_prime to check if a number is prime.
    largest = 1
    for i in range(2, n):
        if n % i == 0:
            if is_prime(i):
                largest = i
    return largest


