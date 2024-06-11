def sort_array(array):
    
    # check for empty array
    if not array:
        return array

    # check for odd or even sum
    if sum(array[0]) + sum(array[-1]) % 2 == 0:
        return sorted(array)
    else:
        return sorted(array, reverse=True)


