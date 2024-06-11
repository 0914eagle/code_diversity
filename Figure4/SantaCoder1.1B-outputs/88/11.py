def sort_array(array):
    
    if len(array) <= 1:
        return array

    if sum(array) % 2 == 0:
        return sort_array(array[::-1])
    else:
        return sort_array(array)


