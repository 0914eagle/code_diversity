

def by_length(arr):
    
    # Check if the array is empty
    if not arr:
        return []

    # Sort the array and reverse it
    sorted_arr = sorted(arr)
    reversed_arr = sorted_arr[::-1]

    # Replace each digit by its corresponding name
    names = []
    for num in reversed_arr:
        if num >= 1 and num <= 9:
            names.append(str(num))
        else:
            names.append('')

    # Return the sorted and reversed array with the corresponding names
    return names


