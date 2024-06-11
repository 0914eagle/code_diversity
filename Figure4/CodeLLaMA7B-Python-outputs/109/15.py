def move_one_ball(arr):
    
    if not arr:
        return True
    if arr[0] < arr[1]:
        return False
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True


