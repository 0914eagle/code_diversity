def hex_key(num):
    
    # Step 1: Create a list of prime numbers
    primes = [2, 3, 5, 7, 11, 13, 17]
    # Step 2: Create a list of hexadecimal digits
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    # Step 3: Create a list of hexadecimal digits that are primes
    hex_primes = [hex_digits[i] for i in primes]
    # Step 4: Count the number of hexadecimal digits that are primes
    count = 0
    for digit in num:
        if digit in hex_primes:
            count += 1
    return count


