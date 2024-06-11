def hex_key(num):
    
    primes = [2, 3, 5, 7, 11, 13, 17]
    count = 0
    for i in num:
        if i in "0123456789":
            count += 1 if int(i) in primes else 0
        else:
            count += 1 if int(i, 16) in primes else 0
    return count