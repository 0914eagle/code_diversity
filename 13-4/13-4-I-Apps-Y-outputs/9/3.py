
def solve(arr):
    n = len(arr)
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the result with the first element
    result = []
    result.append(arr[0])
    # Iterate through the array
    for i in range(1, n):
        # If the current element is equal to the last element of the result, append it to the result
        if arr[i] == result[-1]:
            result.append(arr[i])
        # If the current element is not equal to the last element of the result, start a new block
        else:
            result.append(arr[i])
    return result

