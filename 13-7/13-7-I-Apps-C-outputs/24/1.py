
def solve(n, k, arr):
    # Check if all elements are already equal to k
    if all(elem == k for elem in arr):
        return "yes"
    
    # Check if the sum of all elements is less than k
    if sum(arr) < k:
        return "no"
    
    # Sort the array in non-decreasing order
    arr.sort()
    
    # Initialize the median as the first element
    median = arr[0]
    
    # Loop through the array and check if the median is equal to k
    for i in range(1, n):
        if arr[i] != median:
            return "no"
    
    return "yes"

