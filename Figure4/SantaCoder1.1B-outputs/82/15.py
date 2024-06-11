def prime_length(string):
    
    if len(string) < 2:
        return False
    for i in range(2, len(string)):
        if string[i] % 2 == 0:
            return False
    return True


