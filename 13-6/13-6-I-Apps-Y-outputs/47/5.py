
def get_nice_indices(arr):
    # Calculate the sum of all elements in the array
    sum_of_arr = sum(arr)
    # Initialize an empty list to store the nice indices
    nice_indices = []
    # Iterate over the array
    for i in range(len(arr)):
        # Calculate the sum of all elements except the current element
        sum_of_rest = sum_of_arr - arr[i]
        # Check if the current element is equal to the sum of the rest of the elements
        if arr[i] == sum_of_rest:
            # If it is, add the index of the current element to the list of nice indices
            nice_indices.append(i)
    # Return the list of nice indices
    return nice_indices

