def move_one_ball(arr):
    
    if len(arr) == 0:
        return True
    if len(arr) == 1:
        return True
    if len(arr) == 2:
        if arr[0] < arr[1]:
            return True
        else:
            return False

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True


if