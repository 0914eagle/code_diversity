
def can_partition_array(arr):
    # Calculate the sum of the array
    sum_arr = sum(arr)
    # Check if the sum is divisible by 3
    if sum_arr % 3 != 0:
        return False
    # Calculate the sum of each part
    part_sum = sum_arr // 3
    # Initialize variables to keep track of the current sum and the starting index of the current part
    curr_sum = 0
    start_index = 0
    # Loop through the array
    for i in range(len(arr)):
        # Add the current element to the current sum
        curr_sum += arr[i]
        # If the current sum is equal to the part sum, we have found a valid partition
        if curr_sum == part_sum:
            # Check if the next element is also equal to the part sum
            if i + 1 < len(arr) and arr[i + 1] == part_sum:
                return True
            # Otherwise, reset the current sum and starting index
            curr_sum = 0
            start_index = i + 1
    return False

