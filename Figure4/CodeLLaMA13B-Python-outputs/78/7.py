def hex_key(num):
    
    # Step 1: Create a list of all the hexadecimal digits
    hex_digits = list("0123456789ABCDEF")
    # Step 2: Create a list of all the prime hexadecimal digits
    prime_hex_digits = list("2357BDF")
    # Step 3: Create a list of the hexadecimal digits in the input string
    hex_digits_in_num = list(num)
    # Step 4: Count the number of prime hexadecimal digits in the input string
    count = 0
    for i in hex_digits_in_num:
        if i in prime_hex_digits:
            count += 1
    return count


