
def solve_problem(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the result list
    result = []
    # Iterate through the array
    for i in range(len(arr)):
        # Check if the current element is already present in the result list
        if arr[i] in result:
            # If present, skip the current element
            continue
        # If not present, add the current element to the result list
        result.append(arr[i])
    # Return the result list
    return result

