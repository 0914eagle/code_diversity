def prime_length(string):
    
    string = string.lower()
    for i in range(2, len(string)):
        if string[i] == string[i - 1]:
            return False
    return True


