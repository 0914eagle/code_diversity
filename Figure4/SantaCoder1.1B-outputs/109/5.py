def move_one_ball(arr):
    
    if len(arr) == 0:
        return True
    for i in range(len(arr)):
        if i == 0:
            arr[i] = arr[i] + arr[i+1]
            arr[i+1] = 0
        elif i == len(arr)-1:
            arr[i] = arr[i] + arr[i-1]
            arr[i-1] = 0
        else:
            arr[i] = arr[i] + arr[i-1]
            arr[i-1] = arr[i] + arr[i+1]
            arr[i+1] = 0
    return True

