

def prime_length(string):
    
    # Calculate the length of the string
    string_length = len(string)

    # Check if the length is a prime number
    if string_length == 2 or string_length == 3:
        return True
    for i in range(2, int(string_length ** 0.5) + 1):
        if string_length % i == 0:
            return False
    return True


