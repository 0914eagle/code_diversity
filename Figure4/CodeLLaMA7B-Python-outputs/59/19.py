def largest_prime_factor(n: int):
    
    "*** YOUR CODE HERE ***"
    largest = 1
    while n % 2 == 0:
        largest = 2
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            largest = i
            n = n // i
    if n > 2:
        largest = n
    return largest


