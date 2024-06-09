
def solve(arr):
    # Find the sum of all elements in the array
    sum_of_arr = sum(arr)
    # Initialize a list to store the nice indices
    nice_indices = []
    # Iterate over the array
    for i in range(len(arr)):
        # Calculate the sum of the remaining elements
        sum_of_remaining = sum_of_arr - arr[i]
        # Check if the current element is equal to the sum of the remaining elements
        if arr[i] == sum_of_remaining:
            # If it is, add the index to the list of nice indices
            nice_indices.append(i)
    # Return the list of nice indices
    return nice_indices

