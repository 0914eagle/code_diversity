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
        if arr[0] == arr[3]:
            return 2
        else:
            return 3
    if len(arr) == 5:
        if arr[0] == arr[4]:
            return 3
        else:
            return 4
    if len(arr) == 6:
        if arr[0] == arr[5]:
            return 4
        else:
            return 5
    if len(arr) == 7:
        if arr[0] == arr[6]:
            return 5
        else:
            return 6
    if len(arr) == 8:
        if arr[0] == arr[7]:
            return 6
        else:
            return 7
    if len(arr) == 9:
        if arr[0] == arr[8]:
            return 7
        else:
            return 8
    if len(arr) == 10:
        if arr[0] == arr[9]:
            return 8
        else:
            return 9
    if len(arr) == 11:
        if arr[0] == arr[10]:
            return 9
        else:
            return 10
    if len(arr) == 12:
        if arr[0] == arr[11]:
            return 10
        else:
            return 11
    if len(arr) == 13:
        if arr[0] == arr[12]:
            return 11
        else:
            return 12
    if len(arr) == 14:
        if arr[0] == arr[13