def sort_array(array):
    
    # check for empty array
    if not array:
        return []

    # check if sum of first and last index is even
    if sum(array[0]) % 2 == 0:
        # sort in descending order
        return sorted(array, reverse=True)
    else:
        # sort in ascending order
        return sorted(array)
