def sort_array(array):
    
    if len(array) == 0:
        return array
    if len(array) == 1:
        return array
    if len(array) == 2:
        if sum(array) % 2 == 0:
            return array[::-1]
        else:
            return array
    if len(array) > 2:
        if sum(array[0], array[-1]) % 2 == 0:
            return array[::-1]
        else:
            return array


