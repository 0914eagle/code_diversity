def can_arrange(arr):
    
    # Find the largest element in the array.
    max_val = max(arr)

    # Create a dictionary with keys from 1 to max_val.
    # The values will be the largest index of an element which is not greater
    # than or equal to the element immediately preceding it.
    # If no such element exists then the value will be -1.
    d = {i: -1 for i in range(1, max_val + 1)}

    # Iterate over the array.
    for i, val in enumerate(arr):
        # If the value is greater than or equal to the value of the previous
        # element then set the value of the previous element to the current
        # element.
        if d[val] >= val:
            d[val] = val
        # Otherwise set the value of the previous element to the current index.
        else:
            d[val] = i

    # Iterate over the dictionary.
    for i, val in d.items():
        # If the value is greater than or equal to the value of the previous
        # element then return -1.
        if val >= i:
            return -1

    # Return the largest index of an element which is not greater than or equal
    # to the element immediately preceding it.
    return max(d.values())


print(can_arrange([1, 2, 4, 3, 5]))
print(can_arrange([1, 2, 3]))
