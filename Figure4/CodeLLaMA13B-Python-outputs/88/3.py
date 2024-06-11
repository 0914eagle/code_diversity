def sort_array(array):
    
    if not array:
        return array
    if len(array) == 1:
        return array
    if len(array) == 2:
        return array[::-1] if sum(array) % 2 == 0 else array
    return sorted(array, key=lambda x: x, reverse=sum(array) % 2 == 0)


