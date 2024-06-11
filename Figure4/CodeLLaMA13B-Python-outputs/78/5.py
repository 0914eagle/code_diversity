def hex_key(num):
    
    # Step 1: Create a list of prime numbers
    primes = [2, 3, 5, 7, 11, 13, 17]
    
    # Step 2: Convert the string to a list of hexadecimal digits
    hex_digits = list(num)
    
    # Step 3: Count the number of prime numbers in the list
    count = 0
    for digit in hex_digits:
        if digit in primes:
            count += 1
    
    # Step 4: Return the count
    return count


