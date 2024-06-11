def move_one_ball(arr):
    
    if len(arr) == 0:
        return True
    if len(arr) == 1:
        return True
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return False
        return True
    if len(arr) == 3:
        if arr[0] > arr[1] or arr[1] > arr[2]:
            return False
        return True
    if len(arr) == 4:
        if arr[0] > arr[1] or arr[1] > arr[2] or arr[2] > arr[3]:
            return False
        return True
    if len(arr) == 5:
        if arr[0] > arr[1] or arr[1] > arr[2] or arr[2] > arr[3] or arr[3] > arr[4]:
            return False
        return True
    if len(arr) == 6:
        if arr[0] > arr[1] or arr[1] > arr[2] or arr[2] > arr[3] or arr[3] > arr[4] or arr[4] > arr[5]:
            return False
        return True
    if len(arr) == 7:
        if arr[0] > arr[1] or arr[1] > arr[2] or arr[2] > arr[3] or arr[3] > arr[4] or arr[4] > arr[5] or arr[5] > arr[6]:
            return False
        return True
    if len(arr) == 8:
        if arr[0] > arr[1] or arr[1] > arr[2] or arr[2] > arr[3] or arr[3] > arr[4] or arr[4] > arr[5] or arr[5] > arr[6] or arr[6] > arr[7]:
            return False
        return True
    if len(arr) == 9:
        if arr[0] > arr[1] or arr[1] > arr[2] or arr[2] > arr[3] or arr[3] > arr[4] or arr[4] > arr[5] or arr[5] > arr[6] or arr[6] > arr[7] or arr[7] >