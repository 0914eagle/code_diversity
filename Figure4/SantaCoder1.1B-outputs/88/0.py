def sort_array(array):
    
    if not array:
        return array

    if len(array) == 1:
        return array

    if len(array) == 2:
        if array[0] > array[1]:
            return array
        else:
            return [array[1], array[0]]

    if len(array) % 2 == 0:
        left = sort_array(array[:len(array) // 2])
        right = sort_array(array[len(array) // 2:])
        return merge(left, right)
    else:
        left = sort_array(array[:len(array) // 2])
        right = sort_array(array[len(array) // 2:])
        return merge(left, right[::-1])


