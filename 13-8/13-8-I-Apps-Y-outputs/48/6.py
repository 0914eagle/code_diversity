
def is_sorted_correctly(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    
    # Check if the array is sorted correctly using the described procedure
    for i in range(len(arr) - 1):
        if abs(arr[i] - arr[i+1]) > 1:
            return False
    
    return True

