
def solve(arr):
    # Initialize the sum of non-deleted elements as 0
    sum_non_deleted = 0
    # Initialize the number of elements as the length of the array
    num_elements = len(arr)
    # Initialize the index of the last deleted element as -1
    last_deleted = -1
    # Iterate through the array
    for i in range(num_elements):
        # If the current element is not the last deleted element
        if i != last_deleted:
            # Add the current element to the sum of non-deleted elements
            sum_non_deleted += arr[i]
        # If the current element is the last deleted element
        else:
            # Subtract the current element from the sum of non-deleted elements
            sum_non_deleted -= arr[i]
        # Update the index of the last deleted element
        last_deleted = i
    # Return the sum of non-deleted elements
    return sum_non_deleted

