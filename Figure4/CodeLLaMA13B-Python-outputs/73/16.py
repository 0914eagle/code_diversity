def smallest_change(arr):
    
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        return 1
    # if arr[0] != arr[-1]:
    #     return 1
    # if arr[0] == arr[-1]:
    #     return smallest_change(arr[1:-1])
    # if arr[0] != arr[-1]:
    #     return 1 + min(smallest_change(arr[1:]), smallest_change(arr[:-1]))
    # if arr[0] == arr[-1]:
    #     return smallest_change(arr[1:-1])
    # if arr[0] != arr[-1]:
    #     return 1 + min(smallest_change(arr[1:]), smallest_change(arr[:-1]))
    # if arr[0] == arr[-1]:
    #     return smallest_change(arr[1:-1])
    # if arr[0] != arr[-1]:
    #     return 1 + min(smallest_change(arr[1:]), smallest_change(arr[:-1]))
    # if arr[0] == arr[-1]:
    #     return smallest_change(arr[1:-1])
    # if arr[0] != arr[-1]:
    #     return 1 + min(smallest_change(arr[1:]), smallest_change(arr[:-1]))
    # if arr[0] == arr[-1]:
    #     return smallest_change(arr[1:-1])
    # if arr[0] != arr[-1]:
    #     return 1 + min(smallest_change(arr[1:]), smallest_change(arr[:-1]))
    # if arr[0] == arr[-1]:
    #     return smallest_change(arr[1:-1])
    # if arr[0] != arr[-1]:
    #     return 1 + min(smallest_change(arr[1:]), smallest_change(arr[:-1]))
    # if arr[0] == arr[-1]:
    #     return smallest_change(arr[