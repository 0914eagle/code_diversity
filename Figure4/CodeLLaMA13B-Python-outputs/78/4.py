def hex_key(num):
    
    # Step 1: Create a list of prime numbers
    primes = [2, 3, 5, 7, 11, 13, 17]
    # Step 2: Convert the input string to a list of hexadecimal digits
    hex_list = list(num)
    # Step 3: Iterate through the list of hexadecimal digits
    # Step 3a: If the digit is a prime number, add 1 to the count
    count = 0
    for digit in hex_list:
        if digit in primes:
            count += 1
    # Step 4: Return the count
    return count


