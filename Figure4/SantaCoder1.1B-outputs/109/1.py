def move_one_ball(arr):
    
    if len(arr) == 0:
        return True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            return False
    return True

