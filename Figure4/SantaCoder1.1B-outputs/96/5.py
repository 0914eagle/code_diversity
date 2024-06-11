def count_up_to(n):
    
    # TODO: write your code here
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += 1
            if count == n:
                return primes[:count]
    return primes[:count]


