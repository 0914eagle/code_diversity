def sort_array(array):
    
    if len(array) == 0:
        return array
    if len(array) == 1:
        return array
    else:
        if sum(array[0], array[-1]) % 2 == 0:
            return sorted(array, reverse=True)
        else:
            return sorted(array)


