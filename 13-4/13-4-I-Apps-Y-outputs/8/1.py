
def can_partition_array(arr):
    # Calculate the sum of the array
    sum_arr = sum(arr)
    # Check if the sum is divisible by 3
    if sum_arr % 3 != 0:
        return False
    # Calculate the sum of each part
    part_sum = sum_arr // 3
    # Initialize variables to keep track of the current sum and the index of the current part
    curr_sum = 0
    part_idx = 0
    # Iterate through the array
    for i in range(len(arr)):
        # Add the current element to the current sum
        curr_sum += arr[i]
        # If the current sum is equal to the part sum, move to the next part
        if curr_sum == part_sum:
            part_idx += 1
            curr_sum = 0
        # If the current sum is negative, return False
        elif curr_sum < 0:
            return False
    # If the last part has a non-zero sum, return False
    if curr_sum != 0:
        return False
    # If all the conditions are met, return True
    return True

