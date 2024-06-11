def monotonic(l: list):
    
    if len(l) < 2:
        return True
    for i in range(1, len(l)):
        if l[i] <= l[i - 1]:
            return False
    return True


