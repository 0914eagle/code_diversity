def smallest_change(arr):
    
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        if arr[0] == arr[1]:
            return 0
        else:
            return 1
    if len(arr) == 3:
        if arr[0] == arr[2]:
            return 1
        elif arr[0] == arr[1]:
            return 1
        elif arr[1] == arr[2]:
            return 1
        else:
            return 2
    if len(arr) == 4:
        if arr[0] == arr[3]:
            return 2
        elif arr[0] == arr[2]:
            return 2
        elif arr[0] == arr[1]:
            return 2
        elif arr[1] == arr[2]:
            return 2
        elif arr[1] == arr[3]:
            return 2
        elif arr[2] == arr[3]:
            return 2
        else:
            return 3

    # Find the first occurrence of the smallest element
    min_index = 0
    min_value = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_index = i
            min_value = arr[i]

    # Find the last occurrence of the smallest element
    max_index = 0
    max_value = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_index = i
            max_value = arr[i]

    # If the first and last occurrence are the same, then we need to change all the elements
    # between the first and last occurrence of the smallest element
    if min_index == max_index:
        return len(arr) - 2

    # If the first and last occurrence are not the same, then we need to change all the elements
    # between the first and last occurrence of the smallest element, plus one more element
    return len(arr) - max