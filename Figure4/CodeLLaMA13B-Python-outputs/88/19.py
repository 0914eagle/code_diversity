def sort_array(array):
    
    if not array:
        return array
    if len(array) == 1:
        return array
    if len(array) == 2:
        return [array[0], array[1]] if sum(array) % 2 else [array[1], array[0]]
    return sorted(array, key=lambda x: sum(array[0], x)) if sum(array[0], array[-1]) % 2 else sorted(array, key=lambda x: -sum(array[0], x))
