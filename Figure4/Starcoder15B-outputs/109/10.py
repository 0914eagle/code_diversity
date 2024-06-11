def move_one_ball(arr):
    
    # Your code here
    if len(arr) == 0:
        return True
    if len(arr) == 1:
        return True
    if len(arr) == 2:
        return arr[0] <= arr[1]
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


