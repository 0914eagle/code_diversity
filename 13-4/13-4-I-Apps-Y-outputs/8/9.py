
def can_partition_array(arr):
    # Calculate the sum of the array
    sum_arr = sum(arr)
    # Check if the sum is divisible by 3
    if sum_arr % 3 != 0:
        return False
    # Calculate the sum of each part
    part_sum = sum_arr // 3
    # Initialize the current sum to 0
    current_sum = 0
    # Iterate through the array
    for i in range(len(arr)):
        # Add the current element to the current sum
        current_sum += arr[i]
        # If the current sum is equal to the part sum, set it to 0
        if current_sum == part_sum:
            current_sum = 0
        # If the current sum is negative and greater than the part sum, return False
        elif current_sum > part_sum:
            return False
    # Return True if the last element is 0
    return current_sum == 0

