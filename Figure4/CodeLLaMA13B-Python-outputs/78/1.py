def hex_key(num):
    
    primes = [2, 3, 5, 7, 11, 13, 17]
    hex_digits = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    count = 0
    for i in num:
        if i in primes:
            count += 1
        elif i in hex_digits:
            if hex_digits[i] in primes:
                count += 1
    return count


