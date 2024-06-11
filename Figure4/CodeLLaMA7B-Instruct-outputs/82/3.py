

def prime_length(string):
    
    # Calculate the length of the string
    string_length = len(string)

    # Check if the length is a prime number
    if string_length == 0 or string_length == 1:
        return False
    for i in range(2, string_length):
        if string_length % i == 0:
            return False
    return True


