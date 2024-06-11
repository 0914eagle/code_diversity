def move_one_ball(arr):
    
    # Write your code here
    if len(arr) == 0:
        return True
    if len(arr) == 1:
        return True
    if len(arr) == 2:
        return arr[0] <= arr[1]
    if len(arr) == 3:
        return arr[0] <= arr[1] <= arr[2]
    if len(arr) == 4:
        return arr[0] <= arr[1] <= arr[2] <= arr[3]
    if len(arr) == 5:
        return arr[0] <= arr[1] <= arr[2] <= arr[3] <= arr[4]
    if len(arr) == 6:
        return arr[0] <= arr[1] <= arr[2] <= arr[3] <= arr[4] <= arr[5]
    if len(arr) == 7:
        return arr[0] <= arr[1] <= arr[2] <= arr[3] <= arr[4] <= arr[5] <= arr[6]
    if len(arr) == 8:
        return arr[0] <= arr[1] <= arr[2] <= arr[3] <= arr[4] <= arr[5] <= arr[6] <= arr[7]
    if len(arr) == 9:
        return arr[0] <= arr[1] <= arr[2] <= arr[3] <= arr[4] <= arr[5] <= arr[6] <= arr[7] <= arr[8]
    if len(arr) == 10:
        return arr[0] <= arr[1] <= arr[2] <= arr[3] <= arr[4] <= arr[5] <= arr[6] <= arr[7] <= arr[8] <= arr[9]
    if len(arr) == 11:
        return arr[0] <= arr[1] <= arr[2] <= arr[3] <= arr[4] <= arr[5] <= arr[6] <= arr[7] <= arr[8] <= arr[9] <= arr[10]
    if len(arr) == 12:
        return arr[0] <= arr[1] <= arr[2] <= arr[3] <= arr[4] <= arr[5]