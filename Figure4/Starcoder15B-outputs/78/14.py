def hex_key(num):
    
    hex_digits = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }
    primes = [2, 3, 5, 7, 11, 13]
    count = 0
    for digit in num:
        if hex_digits[digit] in primes:
            count += 1
    return count


