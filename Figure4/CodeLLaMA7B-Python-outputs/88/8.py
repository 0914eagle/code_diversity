def sort_array(array):
    
    # check for empty array
    if not array:
        return []

    # check for odd or even sum
    if sum(array[0]) % 2 == 0:
        array.sort()
    else:
        array.sort(reverse=True)

    return array


