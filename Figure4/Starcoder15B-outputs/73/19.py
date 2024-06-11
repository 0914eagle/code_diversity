def smallest_change(arr):
    
    if arr is None or len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 1
    if len(arr) == 2:
        return 1 if arr[0] != arr[1] else 0
    if is_palindrome(arr):
        return 0
    if len(arr) == 3:
        return 1 if arr[0] == arr[2] else 2
    if len(arr) == 4:
        return 2 if arr[0] == arr[3] and arr[1] == arr[2] else 1
    if len(arr) == 5:
        return 2 if arr[0] == arr[4] and arr[1] == arr[3] else 3
    if len(arr) == 6:
        return 2 if arr[0] == arr[5] and arr[1] == arr[4] and arr[2] == arr[3] else 4
    if len(arr) == 7:
        return 2 if arr[0] == arr[6] and arr[1] == arr[5] and arr[2] == arr[4] else 5
    if len(arr) == 8:
        return 2 if arr[0] == arr[7] and arr[1] == arr[6] and arr[2] == arr[5] and arr[3] == arr[4] else 6
    if len(arr) == 9:
        return 2 if arr[0] == arr[8] and arr[1] == arr[7] and arr[2] == arr[6] and arr[3] == arr[5] else 7
    if len(arr) == 10:
        return 2 if arr[0] == arr[9] and arr[1] == arr[8] and arr[2] == arr[7] and arr[3] == arr[6] and arr[4] == arr[5] else 8
    if len(arr) == 11:
        return 2 if arr[0] == arr[10] and arr[1] == arr[9] and arr[2] == arr[8] and arr[3] == arr[7] and arr[4] == arr