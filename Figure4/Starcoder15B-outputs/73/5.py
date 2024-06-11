def smallest_change(arr):
    
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        return 1 if arr[0] != arr[1] else 0

    # find the middle index
    mid = len(arr) // 2
    # if the length is odd, then the middle index is the one to be changed
    if len(arr) % 2 == 1:
        return 1 + smallest_change(arr[:mid]) + smallest_change(arr[mid + 1:])
    # if the length is even, then the middle two indices are the ones to be changed
    else:
        return smallest_change(arr[:mid]) + smallest_change(arr[mid + 1:])


