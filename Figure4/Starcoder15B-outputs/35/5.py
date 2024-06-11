def max_element(l: list):
    
    if len(l) == 1:
        return l[0]
    else:
        return max(l[0], max_element(l[1:]))


