def sort_array(array):
    
    # check for empty array
    if not array:
        return []

    # check for odd or even sum
    if sum(array[0]) + sum(array[-1]) % 2 == 0:
        # sort in ascending order
        return sorted(array)
    else:
        # sort in descending order
        return sorted(array, reverse=True)
