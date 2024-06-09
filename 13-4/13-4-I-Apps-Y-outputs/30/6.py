
def solve(n, k, arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the minimum number of operations to 0
    min_operations = 0
    # Loop through the array and check if there are at least k equal numbers
    for i in range(n-k+1):
        # If the current element is not equal to the next element, we need to perform an operation
        if arr[i] != arr[i+1]:
            # Calculate the minimum number of operations required to make the current element equal to the next element
            min_operations += arr[i+1] - arr[i]
            # Set the current element to the next element
            arr[i] = arr[i+1]
    return min_operations

