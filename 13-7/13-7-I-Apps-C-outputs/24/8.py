
def solve(n, k, arr):
    # Check if all elements are already equal to k
    if all(x == k for x in arr):
        return "yes"
    
    # Check if it is possible to make all elements equal to k in one operation
    if len(set(arr)) == 1:
        return "no"
    
    # Sort the array in non-decreasing order
    arr.sort()
    
    # Initialize the median of the array
    median = arr[len(arr) // 2]
    
    # Iterate through the array and check if it is possible to make all elements equal to k in one operation
    for i in range(len(arr)):
        if arr[i] != median:
            return "no"
    
    return "yes"

