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
        if array[0] > array[1] and array[1] > array[2]:
            return array
        else:
            return array[::-1]
    if len(array) == 4:
        if array[0] > array[1] and array[1] > array[2] and array[2] > array[3]:
            return array
        else:
            return array[::-1]
    if len(array) == 5:
        if array[0] > array[1] and array[1] > array[2] and array[2] > array[3] and array[3] > array[4]:
            return array
        else:
            return array[::-1]
    if len(array) == 6:
        if array[0] > array[1] and array[1] > array[2] and array[2] > array[3] and array[3] > array[4] and array[4] > array[5]:
            return array
        else:
            return array[::-1]
    if len(array) == 7:
        if array[0] > array[1] and array[1] > array[2] and array[2] > array[3] and array[3] > array[4] and array[4] > array[5] and array[5] > array[6]:
            return array
        else:
            return array[::-1]
    if len(array) == 8:
        if array[0] > array[1] and array[1] > array[2] and array[2] > array[3] and array[3] > array[4] and array[4] > array[5] and array[5] > array[6] and array[6] > array[7]:
            return array
        else:
            return array[::-1]
    if len(array) == 9:
        if array[0] > array[1] and array[1] > array[2] and array[2] > array[3] and array[3