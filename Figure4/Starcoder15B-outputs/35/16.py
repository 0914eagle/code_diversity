def max_element(l: list):
    
    if len(l) == 0:
        return None
    max_element = l[0]
    for i in range(1, len(l)):
        if l[i] > max_element:
            max_element = l[i]
    return max_element


