
def is_sorted(arr):
    # Sort the array in descending order
    arr.sort(reverse=True)
    
    # Check if the array is sorted in ascending order
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return "NO"
    
    return "YES"

