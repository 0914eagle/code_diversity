def max_element(l: list):
    
    max_element = l[0]
    for element in l:
        if element > max_element:
            max_element = element
    return max_element


