def can_arrange(arr):
    
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        if arr[0] <= arr[1]:
            return 0
        else:
            return 1
    if len(arr) == 3:
        if arr[0] <= arr[1] and arr[1] <= arr[2]:
            return 0
        else:
            return 1
    if len(arr) == 4:
        if arr[0] <= arr[1] and arr[1] <= arr[2] and arr[2] <= arr[3]:
            return 0
        else:
            return 1
    if len(arr) == 5:
        if arr[0] <= arr[1] and arr[1] <= arr[2] and arr[2] <= arr[3] and arr[3] <= arr[4]:
            return 0
        else:
            return 1
    if len(arr) == 6:
        if arr[0] <= arr[1] and arr[1] <= arr[2] and arr[2] <= arr[3] and arr[3] <= arr[4] and arr[4] <= arr[5]:
            return 0
        else:
            return 1
    if len(arr) == 7:
        if arr[0] <= arr[1] and arr[1] <= arr[2] and arr[2] <= arr[3] and arr[3] <= arr[4] and arr[4] <= arr[5] and arr[5] <= arr[6]:
            return 0
        else:
            return 1
    if len(arr) == 8:
        if arr[0] <= arr[1] and arr[1] <= arr[2] and arr[2] <= arr[3] and arr[3] <= arr[4] and arr[4] <= arr[5] and arr[5] <= arr[6] and arr[6] <= arr[7]:
            return 0
        else:
            return 1
    if len(arr) == 9:
        if arr[0] <= arr[1] and arr[1] <= arr[2] and arr[2] <= arr[3] and arr[3] <= arr[4