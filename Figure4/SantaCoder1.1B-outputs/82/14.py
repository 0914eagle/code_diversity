def prime_length(string):
    
    for i in range(2, int(math.sqrt(len(string))) + 1):
        if string.count(str(i)) == 0:
            return False
    return True


