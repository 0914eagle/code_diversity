def largest_prime_factor(n: int):
    
    "*** YOUR CODE HERE ***"
    largest_prime = 1
    while n % 2 == 0:
        largest_prime = 2
        n = n // 2
    while n % 3 == 0:
        largest_prime = 3
        n = n // 3
    while n % 5 == 0:
        largest_prime = 5
        n = n // 5
    while n % 7 == 0:
        largest_prime = 7
        n = n // 7
    while n % 11 == 0:
        largest_prime = 11
        n = n // 11
    while n % 13 == 0:
        largest_prime = 13
        n = n // 13
    while n % 17 == 0:
        largest_prime = 17
        n = n // 17
    while n % 19 == 0:
        largest_prime = 19
        n = n // 19
    while n % 23 == 0:
        largest_prime = 23
        n = n // 23
    while n % 29 == 0:
        largest_prime = 29
        n = n // 29
    while n % 31 == 0:
        largest_prime = 31
        n = n // 31
    while n % 37 == 0:
        largest_prime = 37
        n = n // 37
    while n % 41 == 0:
        largest_prime = 41
        n = n // 41
    while n % 43 == 0:
        largest_prime = 43
        n = n // 43
    while n % 47 == 0:
        largest_prime = 47
        n = n // 47
    while n % 53 == 0:
        largest_prime = 53
        n = n // 53
    while n % 59 == 0:
        largest_prime = 59
        n