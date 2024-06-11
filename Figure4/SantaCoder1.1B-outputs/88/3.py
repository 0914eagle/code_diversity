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
            if array[2] > array[1]:
                return array
            else:
                return array[::-1]
        else:
            if array[2] > array[1]:
                return array[::-1]
            else:
                return array

    if len(array) == 4:
        if array[0] > array[1]:
            if array[2] > array[1]:
                if array[3] > array[1]:
                    return array
                else:
                    return array[::-1]
            else:
                if array[3] > array[1]:
                    return array[::-1]
                else:
                    return array
        else:
            if array[2] > array[1]:
                if array[3] > array[1]:
                    return array[::-1]
                else:
                    return array
            else:
                if array[3] > array[1]:
                    return array
                else:
                    return array[::-1]

    if len(array) == 5:
        if array[0] > array[1]:
            if array[2] > array[1]:
                if array[3] > array[1]:
                    if array[4] > array[1]:
                        return array
                    else:
                        return array[::-1]
                else:
                    if array[4] > array[1]:
                        return array[::-1]
                    else:
                        return array
            else:
                if array[3] > array[1]:
                    if array[4] > array[1]:
                        return array[::-1]
                    else:
                        return array
                else:
                    if array[4] > array[1]:
                        return array
                    else:
                        return array[::-1]
        else:
            if array[2] > array[1]:
                if array[3] > array[1]:
                    if array[4] > array[1]:
                        if array[5] > array[1]:
                            return array
                        else:
                            return array[::-1]
                    else:
                        if array[5] > array[1]:
                            return array[::-1]
                        else:
                            return