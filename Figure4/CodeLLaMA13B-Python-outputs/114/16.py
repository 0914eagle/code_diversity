def minSubArraySum(nums):
    
    # 1. get the sum of the array
    # 2. get the sum of the subarray
    # 3. if the subarray sum is less than the array sum, update the array sum
    # 4. return the array sum
    array_sum = sum(nums)
    subarray_sum = 0
    for i in range(len(nums)):
        subarray_sum += nums[i]
        if subarray_sum < array_sum:
            array_sum = subarray_sum
        if subarray_sum > 0:
            subarray_sum = 0
    return array_sum


if