def max_element(l: list):
    
    if len(l) == 0:
        return None
    max_elem = l[0]
    for elem in l:
        if elem > max_elem:
            max_elem = elem
    return max_elem

