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
        else:
            return 2

    if len(arr) == 4:
        if arr[0] == arr[3] and arr[1] == arr[2]:
            return 0
        else:
            return 2

    if len(arr) == 5:
        if arr[0] == arr[4] and arr[1] == arr[3]:
            return 1
        else:
            return 3

    if len(arr) == 6:
        if arr[0] == arr[5] and arr[1] == arr[4] and arr[2] == arr[3]:
            return 0
        else:
            return 2

    if len(arr) == 7:
        if arr[0] == arr[6] and arr[1] == arr[5] and arr[2] == arr[4]:
            return 1
        else:
            return 3

    if len(arr) == 8:
        if arr[0] == arr[7] and arr[1] == arr[6] and arr[2] == arr[5] and arr[3] == arr[4]:
            return 0
        else:
            return 2

    if len(arr) == 9:
        if arr[0] == arr[8] and arr[1] == arr[7] and arr[2] == arr[6] and arr[3] == arr[5]:
            return 1
        else:
            return 3

    if len(arr) == 10:
        if arr[0] == arr[9] and arr[1] == arr[8] and arr[2] == arr[7] and arr[3] == arr[6] and arr[4] == arr[5]:
            return 0
        else:
            return 2

    if len(arr) == 11:
        if arr[0] == arr[10] and arr[1] == arr[9] and arr