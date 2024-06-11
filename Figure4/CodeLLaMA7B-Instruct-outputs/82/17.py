

def prime_length(string):
    
    # Calculate the length of the string
    string_length = len(string)

    # Check if the length is a prime number
    if string_length == 1:
        return True

    # Create a list of prime numbers up to the square root of the string length
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    # Check if the string length is in the list of prime numbers
    if string_length in prime_numbers:
        return True
    else:
        return False


