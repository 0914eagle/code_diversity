def hex_key(num):
    
    # Step 1: Create a list of all the hexadecimal digits
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    
    # Step 2: Create a list of all the prime hexadecimal digits
    prime_hex_digits = ['2', '3', '5', '7', 'B', 'D']
    
    # Step 3: Create a list of the hexadecimal digits in the input string
    hex_digits_in_num = list(num)
    
    # Step 4: Create a list of the prime hexadecimal digits in the input string
    prime_hex_digits_in_num = [digit for digit in hex_digits_in_num if digit in prime_hex_digits]
    
    # Step 5: Return the length of the list of prime hexadecimal digits in the input string
    return len(prime_hex_digits_in_num)
    
    
    
print(hex_key("AB"))
print(hex_key("1077E"))
print(hex_key("ABED1A33"))
print(hex_key("123456789ABCDEF0"))
print(hex_key("2020"))
