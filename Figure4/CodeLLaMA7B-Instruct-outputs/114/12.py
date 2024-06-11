

def minSubArraySum(nums):
    
    # Initialize variables
    min_sum = float('inf')
    current_sum = 0
    start = 0

    # Loop through the array
    for i in range(len(nums)):
        current_sum += nums[i]

        # If the current sum is less than the minimum sum, update the minimum sum
        if current_sum < min_sum:
            min_sum = current_sum

        # If the current sum is greater than the minimum sum, start a new sub-array
        elif current_sum > min_sum:
            start = i + 1
            current_sum = 0

    # Return the minimum sum
    return min(min_sum, current_sum)

# Test the function
