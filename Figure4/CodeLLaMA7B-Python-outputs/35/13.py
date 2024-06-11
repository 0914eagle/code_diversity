def max_element(l: list):
    
    max_element = l[0]
    for i in range(1, len(l)):
        if l[i] > max_element:
            max_element = l[i]
    return max_element


if