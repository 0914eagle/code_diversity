def prime_length(string):
    
    if len(string) == 1:
        return False
    for i in range(2, len(string)):
        if len(string) % i == 0:
            return False
    return True


if