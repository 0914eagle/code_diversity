
def is_unimodal(arr):
    # Check if the array is empty or has only one element
    if len(arr) == 0 or len(arr) == 1:
        return True
    
    # Check if the array is strictly increasing in the beginning
    if arr[0] < arr[1]:
        start = 0
    else:
        start = 1
    
    # Check if the array is constant after the increasing part
    if arr[start] == arr[start+1]:
        constant = start + 1
    else:
        constant = start + 2
    
    # Check if the array is strictly decreasing after the constant part
    if arr[constant] > arr[constant+1]:
        end = constant + 1
    else:
        end = constant + 2
    
    # Check if the array is unimodal
    if end == len(arr):
        return True
    else:
        return False

