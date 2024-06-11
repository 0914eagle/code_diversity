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
        elif arr[1] == arr[2]:
            return 1
        else:
            return 2
    if len(arr) == 4:
        if arr[0] == arr[3]:
            return 2
        elif arr[1] == arr[3]:
            return 2
        elif arr[1] == arr[2]:
            return 1
        else:
            return 3
    if len(arr) == 5:
        if arr[0] == arr[4]:
            return 3
        elif arr[1] == arr[4]:
            return 3
        elif arr[1] == arr[3]:
            return 2
        elif arr[2] == arr[4]:
            return 2
        elif arr[2] == arr[3]:
            return 2
        else:
            return 4
    if len(arr) == 6:
        if arr[0] == arr[5]:
            return 4
        elif arr[1] == arr[5]:
            return 4
        elif arr[1] == arr[4]:
            return 3
        elif arr[2] == arr[5]:
            return 3
        elif arr[2] == arr[4]:
            return 3
        elif arr[2] == arr[3]:
            return 2
        elif arr[3] == arr[4]:
            return 2
        else:
            return 5
    if len(arr) == 7:
        if arr[0] == arr[6]:
            return 5
        elif arr[1] == arr[6]:
            return 5
        elif arr[1] == arr[5]:
            return 4
        elif arr[2] == arr[6]: