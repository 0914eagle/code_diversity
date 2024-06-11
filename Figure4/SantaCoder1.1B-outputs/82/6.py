def prime_length(string):
    
    if len(string) < 2:
        return False
    if len(string) == 2:
        return True
    if string[0] == string[1]:
        return False
    for i in range(2, len(string)):
        if string[i] == string[i-1]:
            return False
    return True


