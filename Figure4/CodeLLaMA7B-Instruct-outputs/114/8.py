

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

        # If the current sum is negative, set it to 0
        if current_sum < 0:
            current_sum = 0

        # If the current index is greater than the start index,
        # remove the first element of the sub-array
        if i > start:
            current_sum -= nums[start]
            start += 1

    return min_sum

#
