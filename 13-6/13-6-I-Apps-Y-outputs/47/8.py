
def get_nice_indices(arr):
    # Calculate the sum of all elements in the array
    sum_of_arr = sum(arr)
    # Initialize an empty list to store the nice indices
    nice_indices = []
    # Iterate over the array
    for i in range(len(arr)):
        # Calculate the sum of all elements except the current element
        sum_of_remaining_elements = sum_of_arr - arr[i]
        # Check if the current element is equal to the sum of remaining elements
        if arr[i] == sum_of_remaining_elements:
            # If it is, add the index of the current element to the nice indices list
            nice_indices.append(i)
    # Return the nice indices list
    return nice_indices

