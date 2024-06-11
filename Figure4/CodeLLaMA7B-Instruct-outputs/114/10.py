

def minSubArraySum(nums):
    
    # Initialize variables
    min_sum = float('inf')
    current_sum = 0
    start = 0

    # Iterate through the array
    for i in range(len(nums)):
        current_sum += nums[i]

        # If the current sum is less than the minimum sum, update the minimum sum
        if current_sum < min_sum:
            min_sum = current_sum

        # If the current sum is greater than the sum of the entire array, reset the current sum
        # to the sum of the first element and move the start index to the next element
        elif current_sum > sum(nums):
            current_sum = nums[start]
            start += 1

    return min_sum

#
