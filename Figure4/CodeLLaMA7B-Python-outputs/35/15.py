def max_element(l: list):
    
    # Your code here
    max_element = l[0]
    for i in l:
        if i > max_element:
            max_element = i
    return max_element


if __name__ == "__