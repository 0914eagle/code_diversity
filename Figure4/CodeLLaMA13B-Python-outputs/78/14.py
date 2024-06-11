def hex_key(num):
    
    primes = [2, 3, 5, 7, 11, 13, 17]
    count = 0
    for i in num:
        if i in primes:
            count += 1
    return count


