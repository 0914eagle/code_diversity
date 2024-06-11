def move_one_ball(arr):
    
    if len(arr) == 0:
        return True
    if len(arr) == 1:
        return True
    if len(arr) == 2:
        return arr[0] <= arr[1]
    if arr[0] <= arr[1]:
        return move_one_ball(arr[1:])
    else:
        return False


