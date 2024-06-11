def sort_array(array):
    
    if len(array) == 0:
        return array

    if len(array) == 1:
        return array

    if len(array) == 2:
        if array[0] > array[1]:
            return array
        else:
            return array[::-1]

    if len(array) == 3:
        if array[0] > array[1]:
            if array[1] > array[2]:
                return array
            else:
                return array[::-1]
        else:
            if array[0] > array[2]:
                return array[::-1]
            else:
                return array

    if len(array) == 4:
        if array[0] > array[1]:
            if array[1] > array[2]:
                if array[2] > array[3]:
                    return array
                else:
                    return array[::-1]
            else:
                if array[0] > array[3]:
                    return array[::-1]
                else:
                    return array
        else:
            if array[0] > array[2]:
                if array[1] > array[3]:
                    return array[::-1]
                else:
                    return array
            else:
                if array[0] > array[3]:
                    return array
                else:
                    return array

    if len(array) == 5:
        if array[0] > array[1]:
            if array[1] > array[2]:
                if array[2] > array[3]:
                    if array[3] > array[4]:
                        return array
                    else:
                        return array[::-1]
                else:
                    return array
            else:
                if array[0] > array[4]:
                    return array[::-1]
                else:
                    return array
        else:
            if array[0] > array[3]:
                if array[1] > array[4]:
                    return array[::-1]
                else:
                    return array
            else:
                if array[0] > array[4]:
                    return array
                else:
                    return array

    if len(array) == 6:
        if array[0] > array[1]:
            if array[1] > array[2]:
                if array[2] > array[3]:
                    if array[3] > array[4]:
                        if array[4] > array[5]:
                            return array
                        else:
                            return array[::-1]
                    else:
                        return array
               