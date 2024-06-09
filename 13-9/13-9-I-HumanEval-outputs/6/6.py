
def hex_key(num: str) -> int:
    
    # Create a list of prime numbers
    prime_numbers = [2, 3, 5, 7, 11, 13, 17]
    
    # Initialize a counter for prime digits
    prime_digit_count = 0
    
    # Iterate through each digit in the input number
    for digit in num:
        # Convert the digit to an integer
        digit_int = int(digit, 16)
        
        # If the digit is a prime number, increment the counter
        if digit_int in prime_numbers:
            prime_digit_count += 1
    
    # Return the count of prime digits
    return prime_digit_count

