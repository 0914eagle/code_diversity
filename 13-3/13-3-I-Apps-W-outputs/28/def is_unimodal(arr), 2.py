
def is_unimodal(arr):
    # Check if the array is empty or has only one element
    if len(arr) == 0 or len(arr) == 1:
        return True
    
    # Check if the array is strictly increasing in the beginning
    if arr[0] > arr[1]:
        return False
    
    # Check if the array is constant after that
    for i in range(1, len(arr) - 1):
        if arr[i] != arr[i + 1]:
            return False
    
    # Check if the array is strictly decreasing after that
    for i in range(len(arr) - 2, 0, -1):
        if arr[i] > arr[i + 1]:
            return False
    
    return True

