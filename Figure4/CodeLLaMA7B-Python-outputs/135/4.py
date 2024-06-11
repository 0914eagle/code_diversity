def can_arrange(arr):
    
    # TODO: Write your solution here
    # O(n) time | O(1) space
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        if arr[0] == arr[1]:
            return 0
        else:
            return -1
    if arr[0] < arr[1]:
        return 0
    if arr[0] == arr[1]:
        return -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return -1
        if arr[i] == arr[i-1]:
            continue
        if arr[i] > arr[i-1]:
            return i-1
    return -1


