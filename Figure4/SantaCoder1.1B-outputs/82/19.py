def prime_length(string):
    
    for i in range(2, len(string)):
        if string[i] % 2 == 0:
            return False
    return True


