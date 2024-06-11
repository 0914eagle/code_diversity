def sort_array(array):
    
    # check for empty array
    if not array:
        return []

    # check for odd or even sum
    if sum(array[0], array[-1]) % 2 == 0:
        # even sum
        return sorted(array, reverse=True)
    else:
        # odd sum
        return sorted(array)
