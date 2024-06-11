def sort_array(array):
    
    if len(array) <= 1:
        return array
    if len(array) == 2:
        if array[0] > array[1]:
            return [array[1], array[0]]
        else:
            return [array[0], array[1]]
    if len(array) % 2 == 0:
        return sort_array(array[0:len(array) // 2]) + sort_array(array[len(array) // 2:])
    else:
        return sort_array(array[0:len(array) // 2]) + sort_array(array[len(array) // 2 + 1:])


if