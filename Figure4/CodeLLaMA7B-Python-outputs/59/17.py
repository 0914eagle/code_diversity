def largest_prime_factor(n: int):
    
    "*** YOUR CODE HERE ***"
    # prime factors are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, ...
    # largest prime factor is the largest prime number that divides n
    # so we can check if n is divisible by 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, ...
    # and return the largest prime number that divides n
    # if n is not divisible by 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, ...
    # then return 1
    # if n is divisible by 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, ...
    # then return the largest prime number that divides n
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    if n % 5 == 0:
        return 5
    if n % 7 == 0:
        return 7
    if n % 11 == 0:
        return 11
    if n % 13 == 0:
        return 13
    if n % 17 == 0:
        return 17
    if n % 19 == 0:
        return 19
    if n % 23 == 0:
        return 23
    if n % 29 == 0:
        return 29
    if n % 31 == 0:
        return 31
    return 1


