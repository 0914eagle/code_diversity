
def is_sorted(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    
    # Check if the array is sorted in non-decreasing order
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return "NO"
    
    return "YES"

