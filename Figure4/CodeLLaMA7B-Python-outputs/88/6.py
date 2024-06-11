def sort_array(array):
    
    # check if array is empty
    if not array:
        return []

    # check if array has only one element
    if len(array) == 1:
        return array

    # check if sum of first and last element is even or odd
    if sum(array[0], array[-1]) % 2 == 0:
        return sorted(array)
    else:
        return sorted(array, reverse=True)
