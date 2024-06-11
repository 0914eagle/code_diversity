def monotonic(l: list):
    
    if len(l) <= 1:
        return True
    if l[0] < l[1]:
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                return False
        return True
    else:
        for i in range(len(l) - 1):
            if l[i] < l[i + 1]:
                return False
        return True


if