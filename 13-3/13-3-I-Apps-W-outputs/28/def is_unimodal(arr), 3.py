
def is_unimodal(arr):
    if len(arr) <= 2:
        return True

    # check if the array is strictly increasing in the beginning
    if arr[0] < arr[1] and arr[1] > arr[2]:
        start_index = 1
    else:
        start_index = 0

    # check if the array is constant after the start index
    for i in range(start_index, len(arr) - 1):
        if arr[i] != arr[i + 1]:
            return False

    # check if the array is strictly decreasing after the start index
    for i in range(start_index, len(arr) - 2, -1):
        if arr[i] > arr[i + 1]:
            return False

    return True

