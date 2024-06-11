def max_element(l: list):
    
    max_element = l[0]
    for i in l:
        if i > max_element:
            max_element = i
    return max_element


print(max_element([1, 2, 3]))
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
