
def get_min_sum(arr):
    # Initialize variables
    n = len(arr)
    sum_of_non_deleted_elements = 0
    last_deleted_element = 0
    is_first_move = True

    # Iterate through the array
    for i in range(n):
        # Check if the current element is even or odd
        if arr[i] % 2 == 0:
            is_even = True
        else:
            is_even = False

        # Check if the current element can be deleted
        if is_first_move or (is_even and last_deleted_element % 2 == 0) or (not is_even and last_deleted_element % 2 == 1):
            # Delete the current element
            sum_of_non_deleted_elements += arr[i]
            last_deleted_element = arr[i]
            is_first_move = False
        else:
            # Break the loop and return the sum of non-deleted elements
            break

    # Return the minimum sum of non-deleted elements
    return sum_of_non_deleted_elements

