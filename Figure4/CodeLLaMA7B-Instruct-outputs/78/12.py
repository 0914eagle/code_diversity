

def hex_key(num):
    

    # Initialize the count of prime digits to 0
    prime_count = 0

    # Iterate over the characters in the input string
    for char in num:
        # Check if the character is a hexadecimal digit
        if char in "0123456789ABCDEF":
            # Convert the character to an integer
            digit = int(char, 16)

            # Check if the digit is a prime number
            if digit > 1 and all(digit % i != 0 for i in range(2, int(digit ** 0.5) + 1)):
                # Increment the count of prime digits
                prime_count += 1

    # Return the count of prime digits
    return prime_count


