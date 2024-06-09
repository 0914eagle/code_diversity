
def is_unimodal(arr):
    # Check if the array is empty or has only one element
    if len(arr) == 0 or len(arr) == 1:
        return True
    
    # Check if the array is strictly increasing in the beginning
    if arr[0] < arr[1]:
        start = 0
    else:
        start = 1
    
    # Check if the array is constant after the beginning
    if all(arr[start] == x for x in arr[start:]):
        return True
    
    # Check if the array is strictly decreasing after the constant part
    if arr[len(arr) - 1] > arr[len(arr) - 2]:
        end = len(arr) - 1
    else:
        end = len(arr) - 2
    
    if all(arr[end] < x for x in arr[:end]):
        return True
    
    return False

