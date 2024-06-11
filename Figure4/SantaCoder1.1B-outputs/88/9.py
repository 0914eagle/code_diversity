def sort_array(array):
    
    if len(array) == 0:
        return array

    if len(array) == 1:
        return array

    if len(array) == 2:
        if array[0] > array[1]:
            return [array[0], array[1]]
        else:
            return [array[1], array[0]]

    if len(array) == 3:
        if array[0] > array[1]:
            if array[2] > array[1]:
                return [array[0], array[1], array[2]]
            else:
                return [array[1], array[0], array[2]]
        else:
            if array[2] > array[1]:
                return [array[1], array[0], array[2]]
            else:
                return [array[0], array[1], array[2]]

    if len(array) == 4:
        if array[0] > array[1]:
            if array[2] > array[1]:
                if array[3] > array[1]:
                    return [array[0], array[1], array[2], array[3]]
                else:
                    return [array[1], array[0], array[2], array[3]]
            else:
                if array[3] > array[1]:
                    return [array[1], array[0], array[2], array[3]]
                else:
                    return [array[0], array[1], array[2], array[3]]
        else:
            if array[2] > array[1]:
                if array[3] > array[1]:
                    return [array[1], array[0], array[2], array[3]]
                else:
                    return [array[0], array[1], array[2], array[3]]
            else:
                if array[3] > array[1]:
                    return [array[0], array[1], array[2], array[3]]
                else:
                    return [array[1], array[0], array[2], array[3]]

    if len(array) == 5:
        if array[0] > array[1]:
            if array[2] > array[1]:
                if array[3] > array[1]:
                    if array[4] > array[1]:
                        return [array[0], array[1], array[2