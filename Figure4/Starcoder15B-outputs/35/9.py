def max_element(l: list):
    
    if len(l) == 0:
        return None
    max_el = l[0]
    for el in l:
        if el > max_el:
            max_el = el
    return max_el


