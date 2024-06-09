
def solve(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the result array
    result = []
    # Loop through the array and check if the current element is equal to the previous element
    for i in range(len(arr)-1):
        # If the current element is equal to the previous element, add it to the result array
        if arr[i] == arr[i+1]:
            result.append(arr[i])
    # Return the result array
    return result

