def smallest_change(arr):
    
    # Your code here
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 1
    if len(arr) == 2:
        return 1 if arr[0] != arr[1] else 0
    if len(arr) == 3:
        return 1 if arr[0] != arr[2] else 0

    if arr[0] == arr[-1]:
        return smallest_change(arr[1:-1])
    else:
        return 1 + min(smallest_change(arr[1:]), smallest_change(arr[:-1]))


