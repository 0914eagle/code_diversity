def sort_array(array):
    
    if not array:
        return array

    if sum(array[0:2]) % 2 == 0:
        return sorted(array)
    else:
        return sorted(array, reverse=True)


