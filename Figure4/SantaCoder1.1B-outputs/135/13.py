def can_arrange(arr):
    
    if len(arr) < 2:
        return -1
    if len(arr) == 2:
        return 1 if arr[0] <= arr[1] else 0
    if arr[0] > arr[1]:
        return 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            return i
    return -1


