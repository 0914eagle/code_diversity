def smallest_change(arr):
    
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        return 1 if arr[0] > arr[1] else 0
    if len(arr) == 3:
        return 2 if arr[0] > arr[1] > arr[2] else 0
    if len(arr) == 4:
        return 3 if arr[0] > arr[1] > arr[2] > arr[3] else 0
    if len(arr) == 5:
        return 4 if arr[0] > arr[1] > arr[2] > arr[3] > arr[4] else 0
    if len(arr) == 6:
        return 5 if arr[0] > arr[1] > arr[2] > arr[3] > arr[4] > arr[5] else 0
    if len(arr) == 7:
        return 6 if arr[0] > arr[1] > arr[2] > arr[3] > arr[4] > arr[5] > arr[6] else 0
    if len(arr) == 8:
        return 7 if arr[0] > arr[1] > arr[2] > arr[3] > arr[4] > arr[5] > arr[6] > arr[7] else 0
    if len(arr) == 9:
        return 8 if arr[0] > arr[1] > arr[2] > arr[3] > arr[4] > arr[5] > arr[6] > arr[7] > arr[8] else 0
    if len(arr) == 10:
        return 9 if arr[0] > arr[1] > arr[2] > arr[3] > arr[4] > arr[5] > arr[6] > arr[7] > arr[8] > arr[9] else 0
    if len(arr) == 11:
        return 10 if arr[0] > arr[1] > arr[2] > arr[3] > arr[4] > arr[5] > arr[6] > arr[7] > arr[8] > arr[9] > arr[10] else 