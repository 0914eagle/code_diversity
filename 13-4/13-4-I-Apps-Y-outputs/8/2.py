
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
    start_idx = 0
    # Loop through the array and check if the current sum is equal to the part sum
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum == part_sum:
            # If the current sum is equal to the part sum, check if the next part is also equal to the part sum
            if i + 1 < len(arr) and sum(arr[i+1:]) == part_sum:
                return True
            # If the current sum is equal to the part sum but the next part is not equal to the part sum, return False
            else:
                return False
        # If the current sum is greater than the part sum, return False
        elif curr_sum > part_sum:
            return False
    # If we reach the end of the array and the current sum is not equal to the part sum, return False
    return False

