def hex_key(num):
    
    # Step 1: Create a list of prime hexadecimal digits
    primes = [2, 3, 5, 7, 11, 13, 17]
    # Step 2: Create a list of hexadecimal digits
    hex_digits = list(num)
    # Step 3: Count the number of hexadecimal digits that are primes
    count = 0
    for digit in hex_digits:
        if int(digit, 16) in primes:
            count += 1
    return count


