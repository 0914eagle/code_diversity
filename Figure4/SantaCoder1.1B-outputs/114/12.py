def minSubArraySum(nums):
    
    # Write your code here
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return min(nums[0], nums[1])
    if len(nums) == 3:
        return min(min(nums[0], nums[1]), nums[2])
    if len(nums) == 4:
        return min(min(min(nums[0], nums[1]), nums[2]), nums[3])
    if len(nums) == 5:
        return min(min(min(min(nums[0], nums[1]), nums[2]), nums[3]), nums[4])
    if len(nums) == 6:
        return min(min(min(min(min(nums[0], nums[1]), nums[2]), nums[3]), nums[4]), nums[5])
    if len(nums) == 7:
        return min(min(min(min(min(min(nums[0], nums[1]), nums[2]), nums[3]), nums[4]), nums[5]), nums[6])
    if len(nums) == 8:
        return min(min(min(min(min(min(min(nums[0], nums[1]), nums[2]), nums[3]), nums[4]), nums[5]), nums[6]), nums[7])
    if len(nums) == 9:
        return min(min(min(min(min(min(min(min(nums[0], nums[1]), nums[2]), nums[3]), nums[4]), nums[5]), nums[6]), nums[7]), nums[8])
    if len(nums) == 10:
        return min(min(min(min(min(min(min(min(min(nums[0], nums[1]), nums[2]), nums[3]), nums[4]), nums[5]), nums[6]), nums[7]), nums[8]), nums[9])
    if len(nums) == 11:
        return min(min(min(min(min(min(min(min(min(min(nums[0], nums[1]), nums[2]), nums[3]), nums[4]), nums[5]), nums[6]),