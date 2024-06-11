


def monotonic(l: list):
    
    if len(l) <= 1:
        return True
    elif l[1] > l[0]:
        for i in range(1, len(l)):
            if l[i] < l[i-1]:
                return False
    elif l[1] < l[0]:
        for i in range(1, len(l)):
            if l[i] > l[i-1]:
                return False
    else:
        return False
    return True


