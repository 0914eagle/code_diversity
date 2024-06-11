def smallest_change(arr):
    
    # Write your code here
    n = len(arr)
    if n == 1:
        return 0
    if n == 2:
        return 1 if arr[0] > arr[1] else 0
    if n == 3:
        return 1 if arr[0] > arr[1] and arr[1] > arr[2] else 0
    if n == 4:
        return 1 if arr[0] > arr[1] and arr[1] > arr[2] and arr[2] > arr[3] else 0
    if n == 5:
        return 1 if arr[0] > arr[1] and arr[1] > arr[2] and arr[2] > arr[3] and arr[3] > arr[4] else 0
    if n == 6:
        return 1 if arr[0] > arr[1] and arr[1] > arr[2] and arr[2] > arr[3] and arr[3] > arr[4] and arr[4] > arr[5] else 0
    if n == 7:
        return 1 if arr[0] > arr[1] and arr[1] > arr[2] and arr[2] > arr[3] and arr[3] > arr[4] and arr[4] > arr[5] and arr[5] > arr[6] else 0
    if n == 8:
        return 1 if arr[0] > arr[1] and arr[1] > arr[2] and arr[2] > arr[3] and arr[3] > arr[4] and arr[4] > arr[5] and arr[5] > arr[6] and arr[6] > arr[7] else 0
    if n == 9:
        return 1 if arr[0] > arr[1] and arr[1] > arr[2] and arr[2] > arr[3] and arr[3] > arr[4] and arr[4] > arr[5] and arr[5] > arr[6] and arr[6] > arr[7] and arr[7] > arr[8] else 0
    if n == 10:
        return 1 if arr[0