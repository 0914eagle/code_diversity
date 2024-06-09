
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
    if all(arr[start] == x for x in arr[start:]):
        return True
    
    # Check if the array is strictly decreasing after the constant part
    if arr[start:] == sorted(arr[start:], reverse=True):
        return True
    
    return False

