def smallest_change(arr):
    
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        return 1 if arr[0] > arr[1] else 0
    if len(arr) == 3:
        return 1 if arr[0] > arr[1] and arr[0] > arr[2] else 0
    if len(arr) == 4:
        return 1 if arr[0] > arr[1] and arr[0] > arr[2] and arr[0] > arr[3] else 0
    if len(arr) == 5:
        return 1 if arr[0] > arr[1] and arr[0] > arr[2] and arr[0] > arr[3] and arr[0] > arr[4] else 0
    if len(arr) == 6:
        return 1 if arr[0] > arr[1] and arr[0] > arr[2] and arr[0] > arr[3] and arr[0] > arr[4] and arr[0] > arr[5] else 0
    if len(arr) == 7:
        return 1 if arr[0] > arr[1] and arr[0] > arr[2] and arr[0] > arr[3] and arr[0] > arr[4] and arr[0] > arr[5] and arr[0] > arr[6] else 0
    if len(arr) == 8:
        return 1 if arr[0] > arr[1] and arr[0] > arr[2] and arr[0] > arr[3] and arr[0] > arr[4] and arr[0] > arr[5] and arr[0] > arr[6] and arr[0] > arr[7] else 0
    if len(arr) == 9:
        return 1 if arr[0] > arr[1] and arr[0] > arr[2] and arr[0] > arr[3] and arr[0] > arr[4] and arr[0] > arr[5] and arr[0] > arr[6] and arr[0] > arr[7] and arr[0] > arr[8] else 0
    if