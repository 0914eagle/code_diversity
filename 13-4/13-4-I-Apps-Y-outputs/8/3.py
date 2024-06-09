
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
        # If the current sum is equal to the part sum, we have found a valid partition
        if current_sum == part_sum:
            # If it is the first element, we need to make sure that the next element is not 0
            if i == 0:
                if arr[i+1] != 0:
                    current_sum = 0
                    continue
            # If it is the last element, we need to make sure that the previous element is not 0
            elif i == len(arr) - 1:
                if arr[i-1] != 0:
                    current_sum = 0
                    continue
            # If it is any other element, we need to make sure that the previous and next elements are not 0
            else:
                if arr[i-1] != 0 and arr[i+1] != 0:
                    current_sum = 0
                    continue
        # If the current sum is greater than the part sum, we need to backtrack
        elif current_sum > part_sum:
            current_sum = 0
    # If the current sum is not 0 at the end of the iteration, it means that we have found a valid partition
    if current_sum != 0:
        return True
    else:
        return False

