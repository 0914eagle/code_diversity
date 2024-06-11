def prime_length(string):
    
    if len(string) == 1:
        return True
    if len(string) == 2:
        return False
    if len(string) % 2 == 0:
        return False
    for i in range(3, int(len(string)**0.5)+1, 2):
        if string.count(i) > 1:
            return False
    return True


