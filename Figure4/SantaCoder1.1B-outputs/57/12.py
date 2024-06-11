def monotonic(l: list):
    
    if len(l) == 0:
        return True
    if len(l) == 1:
        return l[0] > l[0]
    if l[0] > l[1]:
        return False
    if l[0] < l[1]:
        return True
    return monotonic(l[1:])


